from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow, QFileDialog

from design.mainwindow import Ui_MainWindow
from hardware.status import Intervals
from ui.table_model import SinglePhotoGateTableModel, DoublePhotoGateTableModel, CheckpointPhotoGateTableModel, \
    ExpPhotoGateTableModel
from ui.ui_controller import UIControllerMain

import signal

signal.signal(signal.SIGINT, signal.SIG_DFL)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.ctrl = UIControllerMain()

        self.ctrl.connection_changed.connect(self._on_connection_changed)
        self.ctrl.intervals_changed.connect(self._on_intervals_update)
        self.ctrl.pg_model0_changed.connect(self._on_table0_update)
        self.ctrl.pg_model1_changed.connect(self._on_table1_update)
        self.ctrl.pg_models_changed.connect(self._on_table_update)
        self.ctrl.checkpoint_model_changed.connect(self._on_checkpoint_table_update)
        self.ctrl.exp_model_changed.connect(self._on_exp_table_update)

        self.pg_single_model = SinglePhotoGateTableModel(self)
        self.pg_single_model.install(self.table_0)

        self.pg_double_model = DoublePhotoGateTableModel(self)
        self.pg_double_model.install(self.table_1)

        self.pg_timed_model = CheckpointPhotoGateTableModel(self)
        self.pg_timed_model.install(self.table_cnts)

        self.pg_exp_model = ExpPhotoGateTableModel(self)
        self.pg_exp_model.install(self.table_exp)

        self.button_time_reset.clicked.connect(self._reset_time)
        self.button_save_s.clicked.connect(self._save_single)
        self.button_save_d.clicked.connect(self._save_double)

        self.button_add.clicked.connect(lambda x: self.ctrl.timed_store())
        self.button_save_t.clicked.connect(self._save_timed)

        self.autoStore.stateChanged.connect(
            lambda: self.ctrl.change_timer(self.autoStore.isChecked(), self.timeFreq.value())
        )

        self.exp_run.stateChanged.connect(lambda x: self.ctrl.exp_run(self.exp_run.isChecked()))
        self.exp_save.clicked.connect(self._save_exp)

        self.on_checkbox.stateChanged.connect(lambda x: self.ctrl.data.enable(x))

        self.button_clear.clicked.connect(self.clear)

        self.ctrl.start()

    def clear(self):
        self.ctrl.reset()
        self.pg_single_model.clear()
        self.pg_double_model.replace([])
        self.pg_timed_model.replace([])
        self.pg_exp_model.replace([])

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

    def _save_exp(self):
        filename = self._file_path_dialog()
        if filename is None:
            return
        self.ctrl.save_csv_exp(filename)

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

    def _on_table0_update(self, row):
        self.pg_single_model.append(row)
        self.table_0.scrollToBottom()

    def _on_table1_update(self, row):
        self.pg_double_model.append(row)
        self.table_1.scrollToBottom()

    def _on_checkpoint_table_update(self, row):
        self.pg_timed_model.append(row)
        self.table_cnts.scrollToBottom()

    def _on_exp_table_update(self, row):
        self.pg_exp_model.append(row)
        self.table_exp.scrollToBottom()

    def _reset_time(self):
        self.ctrl.reset_time()

    def closeEvent(self, event):
        self.ctrl.stop()
        self.ctrl.terminate()
        event.accept()
