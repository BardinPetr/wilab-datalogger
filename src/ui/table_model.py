from PySide6 import QtCore
from PySide6.QtCore import Qt, QAbstractTableModel

from processing.photogate import TickHistoryItem


class ListTableModel(QAbstractTableModel):
    def __init__(self, parent, header):
        QAbstractTableModel.__init__(self, parent)
        self.contents = []
        self._header = header

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
            return self.contents[index.row()][index.column()]

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


class ZipListTableModel(QAbstractTableModel):
    def __init__(self, parent, header):
        QAbstractTableModel.__init__(self, parent)
        self.column_lists = [[] for _ in range(len(header))]
        self._header = ["№", *header]

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
    def __init__(self, parent, header):
        super().__init__(parent, header)

    def present_cell_by_column(self, col, value: TickHistoryItem):
        return round(value.ts.timestamp() * 1000)