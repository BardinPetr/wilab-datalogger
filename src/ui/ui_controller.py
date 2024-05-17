import csv
from datetime import datetime
from itertools import zip_longest

from PySide6.QtCore import Signal, QThread, QTimer

from hardware.status import Intervals
from processing.datalogger import PhotoGateDatalogger
from processing.interface import InterfaceController

from processing.pg_exp_datalogger import PhotoGateExpDatalogger
from processing.pg_pairing_datalogger import PhotoGatePairingDatalogger
from ui.table_model import CheckpointPhotoGateTableModel, ExpPhotoGateTableModel


def save_csv(filename, headers, data):
    with open(filename, 'w') as f:
        wr = csv.writer(f)
        wr.writerow(headers)
        wr.writerows(data)


class UIControllerMain(QThread):
    connection_changed = Signal(bool)
    intervals_changed = Signal(Intervals, Intervals)
    pg_model0_changed = Signal(list)
    pg_model1_changed = Signal(list)
    pg_models_changed = Signal(list, list)
    checkpoint_model_changed = Signal(list)
    exp_model_changed = Signal(list)

    def __init__(self):
        super().__init__()
        self.ctrl = InterfaceController(
            lambda conn_state: self.connection_changed.emit(conn_state),
        )

        self.data = PhotoGatePairingDatalogger(self.ctrl)
        self.data.subscribe(lambda a, b: self.pg_models_changed.emit(a, b))
        # self.data.subscribe(self.push_main_tables)

        self.exp = PhotoGateExpDatalogger(self.ctrl)
        self.exp.subscribe(
            lambda table: self.exp_model_changed.emit(table)
        )

        self.checkpoints = []

        self.store_timer = QTimer(self)
        self.store_timer.timeout.connect(self.timed_store)

        self.update_timer = QTimer(self)
        self.update_timer.timeout.connect(self.update_intervals)
        self.update_timer.start(100)

    def push_main_tables(self, t0row, t1row):
        if t0row:
            self.pg_model0_changed.emit(t0row)
        if t1row:
            self.pg_model0_changed.emit(t1row)

    def update_intervals(self):
        self.intervals_changed.emit(*self.ctrl.get())

    def reset_time(self):
        self.data.zero_time()

    def save_csv_single(self, filename):
        data = list(zip_longest(
            *[
                [i.relative_ms for i in column]
                for column in self.data.tick_history
            ],
            fillvalue=''
        ))
        save_csv(
            filename,
            ["время 1 ворота (мс.)", "время 2 ворота (мс.)"],
            data
        )

    def save_csv_double(self, filename):
        data = [
            [i.start_relative, i.end_relative]
            for i in self.data.pair_history
        ]
        save_csv(
            filename,
            ["время 1 ворота (мс.)", "время 2 ворота (мс.)"],
            data
        )

    def save_csv_timed(self, filename):
        save_csv(
            filename,
            CheckpointPhotoGateTableModel.HEADER,
            self.checkpoints
        )

    def save_csv_exp(self, filename):
        save_csv(
            filename,
            ExpPhotoGateTableModel.HEADER,
            self.exp.history
        )

    def timed_store(self):
        data = [
            [i.counter, i.time_up, i.time_down, i.interval_up_front, i.interval_down_front]
            for i in self.ctrl.get()
        ]
        row = (
            round(datetime.now().timestamp() * 1000),
            *data[0], *data[1]
        )
        self.checkpoints.append(row)
        self.checkpoint_model_changed.emit(row)

    def change_timer(self, enable, freq_hz):
        if not enable:
            self.store_timer.stop()
            return

        int_ms = 1000 // freq_hz
        self.store_timer.start(int_ms)

    def exp_run(self, start):
        if start:
            self.exp.begin()
        else:
            self.exp.end()

    def reset(self):
        self.checkpoints = []
        self.data.reset()
        self.exp.reset()

    def run(self):
        self.ctrl.start()

    def stop(self):
        self.ctrl.stop()
