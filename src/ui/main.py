from PySide6.QtWidgets import QMainWindow

from design.mainwindow import Ui_MainWindow
from hardware.status import Intervals
from ui.table_model import SinglePhotoGateTableModel, ListTableModel, DoublePhotoGateTableModel
from ui_controller import UIControllerMain


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.ctrl = UIControllerMain()

        self.ctrl.connection_changed.connect(self._on_connection_changed)
        self.ctrl.intervals_changed.connect(self._on_intervals_update)
        self.ctrl.pg_models_changed.connect(self._on_table_update)

        self.pg_single_model = SinglePhotoGateTableModel(self, ["Ворота 1, мс", "Ворота 2, мс"])
        self.table_0.setModel(self.pg_single_model)

        self.pg_double_model = DoublePhotoGateTableModel(self, ["№", "Ворота 1, мс", "Ворота 2, мс", "Промежуток, мс"])
        self.table_1.setModel(self.pg_double_model)

        # timer = QTimer(self)
        # timer.timeout.connect(self._on_table_update)
        # timer.start(500)

        self.button_time_reset.clicked.connect(self._reset_time)

        self.ctrl.start()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)

    def _on_connection_changed(self, is_connected):
        self.connectionLabel.setText("Connected" if is_connected else "Disconnected")

    def _on_intervals_update(self, interval0: Intervals, interval1: Intervals):
        for uid, data in enumerate([interval0, interval1]):
            for field in ['counter', 'interval_up_front', 'interval_down_front', 'time_up', 'time_down']:
                getattr(self, f"value_{uid}_{field}").display(getattr(data, field))

    def _on_table_update(self, pg_single_list, pg_double_list):
        self.pg_single_model.replace(pg_single_list)
        self.pg_double_model.replace(pg_double_list)
        self.table_0.scrollToBottom()
        self.table_1.scrollToBottom()

    def _reset_time(self):
        self.ctrl.reset_time()
