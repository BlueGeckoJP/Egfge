from PySide6 import QtWidgets

from widgets import filesystemtree, groupswidget, placelist


class LeftPanelTabWidget(QtWidgets.QTabWidget):
    def __init__(self, *args, **kwargs):
        super(LeftPanelTabWidget, self).__init__(*args, **kwargs)

        self.place_list = placelist.PlaceList()
        self.file_system_tree = filesystemtree.FileSystemTree()
        self.groups_widget = groupswidget.GroupsWidget()

        self.insertTab(0, self.place_list, "Places")
        self.insertTab(1, self.file_system_tree, "Files")
        self.insertTab(1, self.groups_widget, "Groups")
