import csv
from itertools import zip_longest

from PySide6.QtCore import Signal, QThread

from hardware.status import Intervals
from processing.interface import InterfaceController
from processing.photogate import PhotoGateDatalogger


def save_csv(filename, headers, data):
    with open(filename, 'w') as f:
        wr = csv.writer(f)
        wr.writerow(headers)
        wr.writerows(data)


class UIControllerMain(QThread):
    connection_changed = Signal(bool)
    intervals_changed = Signal(Intervals, Intervals)
    pg_models_changed = Signal(list, list)

    def __init__(self):
        super().__init__()
        self.ctrl = InterfaceController(
            lambda conn_state: self.connection_changed.emit(conn_state),
            lambda intervals: self.intervals_changed.emit(*intervals)
        )
        self.data = PhotoGateDatalogger(self.ctrl.counters)
        self.data.subscribe(self._on_update_pg)

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
        pass

    def run(self):
        self.ctrl.start()
