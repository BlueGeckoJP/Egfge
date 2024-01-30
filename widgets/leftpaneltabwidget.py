from PySide6 import QtWidgets

from widgets import groupswidget, placelist


class LeftPanelTabWidget(QtWidgets.QTabWidget):
    def __init__(self, *args, **kwargs):
        super(LeftPanelTabWidget, self).__init__(*args, **kwargs)

        self.place_list = placelist.PlaceList()
        self.groups_widget = groupswidget.GroupsWidget()

        self.insertTab(0, self.place_list, "Places")
        self.insertTab(1, self.groups_widget, "Groups")
