from PySide6 import QtGui, QtWidgets


class PlaceList(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        label = QtWidgets.QLabel()
        label.setText("Places")
        label.setAlignment(
            QtGui.Qt.AlignmentFlag.AlignVCenter | QtGui.Qt.AlignmentFlag.AlignLeft
        )

        self.list_view = ListView()

        widget_layout = QtWidgets.QVBoxLayout()
        widget_layout.addWidget(label)
        widget_layout.addWidget(self.list_view)

        self.setLayout(widget_layout)


class ListView(QtWidgets.QListView):
    def __init__(self, *args, **kwargs):
        super(ListView, self).__init__(*args, **kwargs)

        self.item_model = QtGui.QStandardItemModel(self)

        self.setModel(self.item_model)
        self.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)

        place_list = [
            "Home",
            "Desktop",
            "Documents",
            "Downloads",
            "Music",
            "Pictures",
            "Videos",
        ]

        for place in place_list:
            item = QtGui.QStandardItem()
            item.setText(place)
            self.item_model.appendRow(item)
