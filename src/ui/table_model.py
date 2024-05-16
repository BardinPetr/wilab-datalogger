from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Qt, QAbstractTableModel

from processing.pg_pairing_datalogger import PairHistoryItem, TickHistoryItem


class BaseTableModel(QAbstractTableModel):

    def __init__(self, parent, header):
        QAbstractTableModel.__init__(self, parent)
        self._header = ["№", *header]

    def install(self, table, auto_size=True):
        table.setModel(self)
        if auto_size:
            table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)


class ListTableModel(BaseTableModel):
    def __init__(self, parent, header):
        super().__init__(parent, header)
        self.contents = []

    def update(self, start_row=0, end_row=0):
        self.layoutAboutToBeChanged.emit()
        self.dataChanged.emit(
            self.createIndex(start_row, 0),
            self.createIndex(end_row if end_row else self.rowCount(0), self.columnCount(0))
        )
        self.layoutChanged.emit()

    def rowCount(self, parent=...):
        return len(self.contents)

    def columnCount(self, parent=...):
        return len(self._header)

    def data(self, index, role=...):
        if not index.isValid():
            return None

        if role == QtCore.Qt.DisplayRole:
            row, col = index.row(), index.column()
            return self.present_cell(row, col)

    def present_cell(self, row, col):
        return self.contents[row][col]

    def headerData(self, col, orientation, role=...):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._header[col]
        return None

    def setData(self, index, value, role=...):
        if not index.isValid():
            return False
        self.dataChanged.emit(index, index)
        return True

    def append(self, row):
        self.contents.append(row)
        self.update(len(self.contents) - 1, len(self.contents))

    def replace(self, data):
        self.contents = data[:]
        self.update()


class ZipListTableModel(BaseTableModel):
    def __init__(self, parent, header):
        super().__init__(parent, header)
        self.column_lists = [[] for _ in range(len(header))]

    def update(self, start_row=0, end_row=0):
        self.layoutAboutToBeChanged.emit()
        self.dataChanged.emit(
            self.createIndex(start_row, 0),
            self.createIndex(end_row if end_row else self.rowCount(0), self.columnCount(0))
        )
        self.layoutChanged.emit()

    def rowCount(self, parent=...):
        return len(max(self.column_lists, key=len))

    def columnCount(self, parent=...):
        return len(self._header)

    def data(self, index, role=...):
        if not index.isValid():
            return None

        if role == QtCore.Qt.DisplayRole:
            row, col = index.row(), index.column() - 1
            if col == -1:
                return row + 1
            column = self.column_lists[col]
            if row >= len(column):
                return '-'
            return self.present_cell_by_column(col, column[row])

    def present_cell_by_column(self, col, value):
        return value

    def headerData(self, col, orientation, role=...):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._header[col]
        return None

    def append(self, row):
        self.column_lists.append(row)
        self.update(len(self.column_lists) - 1, len(self.column_lists))

    def replace(self, data):
        self.column_lists = data[:]
        self.update()


class SinglePhotoGateTableModel(ZipListTableModel):
    HEADER = ["Ворота 1, мс", "Ворота 2, мс"]

    def __init__(self, parent):
        super().__init__(parent, self.HEADER)

    def present_cell_by_column(self, col, value: TickHistoryItem):
        return round(value.relative_ms)


class DoublePhotoGateTableModel(ListTableModel):
    HEADER = ["Ворота 1, мс", "Ворота 2, мс", "Промежуток, мс"]

    def __init__(self, parent):
        super().__init__(parent, self.HEADER)

    def present_cell(self, row, col):
        value: PairHistoryItem = self.contents[row]
        match col:
            case 0:
                return row + 1
            case 1:
                return value.start_relative
            case 2:
                return value.end_relative
            case 3:
                return value.duration


class CheckpointPhotoGateTableModel(ListTableModel):
    HEADER = [
        "time ms", *[f"{n} {i}" for i in range(1, 3) for n in ("cnt", "up-down", "down-up", "up-up", "down-down")]
    ]

    def __init__(self, parent):
        super().__init__(parent, self.HEADER)

    def present_cell(self, row, col):
        if col == 0:
            return row + 1
        return self.contents[row][col - 1]


class ExpPhotoGateTableModel(ListTableModel):
    HEADER = ["Время Л1, мс", "Длительность Л1, мс", "Время П1, мс",
              "Длительность П1, мс", "Время Л2, мс", "Длительность Л2, мс",
              "Время П2, мс", "Длительность П2, мс"]

    def __init__(self, parent):
        super().__init__(parent, self.HEADER)

    def present_cell(self, row, col):
        if col == 0:
            return row + 1
        return self.contents[row][col - 1]
