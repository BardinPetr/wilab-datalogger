from itertools import zip_longest

from PySide6.QtCore import Signal, QThread

from hardware.status import Intervals
from processing.interface import InterfaceController
from processing.photogate import PhotoGateDatalogger


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

    def run(self):
        self.ctrl.start()
