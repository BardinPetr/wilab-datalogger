from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow, QFileDialog

from design.mainwindow import Ui_MainWindow
from hardware.status import Intervals
from ui.table_model import SinglePhotoGateTableModel, DoublePhotoGateTableModel, CheckpointPhotoGateTableModel
from ui.ui_controller import UIControllerMain, CHECKPOINT_TABLE_HEADERS


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.ctrl = UIControllerMain()

        self.ctrl.connection_changed.connect(self._on_connection_changed)
        self.ctrl.intervals_changed.connect(self._on_intervals_update)
        self.ctrl.pg_models_changed.connect(self._on_table_update)
        self.ctrl.checkpoint_model_changed.connect(self._on_checkpoint_table_update)

        self.pg_single_model = SinglePhotoGateTableModel(self, ["Ворота 1, мс", "Ворота 2, мс"])
        self.table_0.setModel(self.pg_single_model)

        self.pg_double_model = DoublePhotoGateTableModel(self, ["№", "Ворота 1, мс", "Ворота 2, мс", "Промежуток, мс"])
        self.table_1.setModel(self.pg_double_model)

        self.pg_timed_model = CheckpointPhotoGateTableModel(self, CHECKPOINT_TABLE_HEADERS)
        self.table_cnts.setModel(self.pg_timed_model)
        self.table_cnts.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)

        self.button_time_reset.clicked.connect(self._reset_time)
        self.button_save_s.clicked.connect(self._save_single)
        self.button_save_d.clicked.connect(self._save_double)

        self.button_add.clicked.connect(lambda x: self.ctrl.timed_store())
        self.button_save_t.clicked.connect(self._save_timed)

        self.ctrl.start()

    def _file_path_dialog(self):
        filepath, _ = QFileDialog.getSaveFileName(self, "Save CSV", filter="CSV files (*.csv)")
        if not filepath:
            return None

        return filepath if filepath.endswith(".csv") else (filepath + ".csv")

    def _save_single(self):
        filename = self._file_path_dialog()
        if filename is None:
            return
        self.ctrl.save_csv_single(filename)

    def _save_double(self):
        filename = self._file_path_dialog()
        if filename is None:
            return
        self.ctrl.save_csv_double(filename)

    def _save_timed(self):
        filename = self._file_path_dialog()
        if filename is None:
            return
        self.ctrl.save_csv_timed(filename)

    def _on_connection_changed(self, is_connected):
        self.connectionLabel.setText("Connected" if is_connected else "Disconnected")

    def _on_intervals_update(self, interval0: Intervals, interval1: Intervals):
        self.value_0_counter.display(interval0.counter)
        self.value_1_counter.display(interval1.counter)
        for uid, data in enumerate([interval0, interval1]):
            for field in ['interval_up_front', 'interval_down_front', 'time_up', 'time_down']:
                getattr(self, f"value_{uid}_{field}").setText(f"{getattr(data, field):0.3f} c")

    def _on_table_update(self, pg_single_list, pg_double_list):
        self.pg_single_model.replace(pg_single_list)
        self.pg_double_model.replace(pg_double_list)
        self.table_0.scrollToBottom()
        self.table_1.scrollToBottom()

    def _on_checkpoint_table_update(self, table):
        self.pg_timed_model.replace(table)
        self.table_cnts.scrollToBottom()

    def _reset_time(self):
        self.ctrl.reset_time()
