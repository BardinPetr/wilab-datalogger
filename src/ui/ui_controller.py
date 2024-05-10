import csv
from datetime import datetime
from itertools import zip_longest

from PySide6.QtCore import Signal, QThread

from hardware.status import Intervals
from processing.interface import InterfaceController
from processing.photogate import PhotoGateDatalogger

CHECKPOINT_TABLE_HEADERS = [
    "№", "time ms", *[f"{n} {i}" for i in range(1, 3) for n in ("cnt", "up-down", "down-up", "up-up", "down-down")]
]


def save_csv(filename, headers, data):
    with open(filename, 'w') as f:
        wr = csv.writer(f)
        wr.writerow(headers)
        wr.writerows(data)


class UIControllerMain(QThread):
    connection_changed = Signal(bool)
    intervals_changed = Signal(Intervals, Intervals)
    pg_models_changed = Signal(list, list)
    checkpoint_model_changed = Signal(list)

    def __init__(self):
        super().__init__()
        self.ctrl = InterfaceController(
            lambda conn_state: self.connection_changed.emit(conn_state),
            lambda intervals: self.intervals_changed.emit(*intervals)
        )
        self.data = PhotoGateDatalogger(self.ctrl.counters)
        self.data.subscribe(self._on_update_pg)

        self.checkpoints = []

    def _on_update_pg(self, s_histories, d_histories):
        self.pg_models_changed.emit(s_histories, d_histories)

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
            CHECKPOINT_TABLE_HEADERS[1:],
            self.checkpoints
        )

    def timed_store(self):
        data = [
            [i.counter, i.time_up, i.time_down, i.interval_up_front, i.interval_down_front]
            for i in self.ctrl.get()
        ]
        self.checkpoints.append((
            round(datetime.now().timestamp() * 1000),
            *data[0], *data[1]
        ))
        self.checkpoint_model_changed.emit(self.checkpoints)

    def run(self):
        self.ctrl.start()
