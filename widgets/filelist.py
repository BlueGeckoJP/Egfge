from PySide6 import QtGui, QtWidgets


class FileList(QtWidgets.QTableView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.item_model = QtGui.QStandardItemModel(self)
        self.item_model.setHorizontalHeaderLabels(["名前", "サイズ", "変更日時"])

        self.setModel(self.item_model)
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setSectionResizeMode(
            0, QtWidgets.QHeaderView.ResizeMode.Stretch
        )
        self.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
