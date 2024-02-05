from PySide6 import QtGui, QtWidgets


class GroupsWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.list_view = ListView()

        self.combo_box = ComboBox()

        top_contents_layout = QtWidgets.QHBoxLayout()
        top_contents_layout.addWidget(self.combo_box)

        widget_layout = QtWidgets.QVBoxLayout()
        widget_layout.addLayout(top_contents_layout)
        widget_layout.addWidget(self.list_view)

        self.setLayout(widget_layout)


class ListView(QtWidgets.QListView):
    def __init__(self, *args, **kwargs):
        super(ListView, self).__init__(*args, **kwargs)

        self.item_model = QtGui.QStandardItemModel(self)

        self.setModel(self.item_model)
        self.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)


class ComboBox(QtWidgets.QComboBox):
    def __init__(self, *args, **kwargs):
        super(ComboBox, self).__init__(*args, **kwargs)

        self.setEditable(False)

        self.addItem("自動")
        self.addItem("手動")
