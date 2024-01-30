import datetime
import glob
import math
import os
import sys

from PySide6 import QtGui, QtWidgets

from widgets import filelist, leftpaneltabwidget

current_path = os.path.expanduser("~")
moving_history: list[str] = [os.path.expanduser("~")]
current_moving_index = 0

places_path_list = [
    "~",
    "~/Desktop",
    "~/Documents",
    "~/Downloads",
    "~/Music",
    "~/Pictures",
    "~/Videos",
]


class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Egfge")
        self.resize(1000, 600)

        # Definition Layouts ==================================================
        top_layout = QtWidgets.QVBoxLayout()
        topbar_layout = QtWidgets.QHBoxLayout()
        central_layout = QtWidgets.QHBoxLayout()
        leftpanel_layout = QtWidgets.QVBoxLayout()
        file_layout = QtWidgets.QVBoxLayout()

        # Definition Widgets ==================================================
        before_button = QtWidgets.QPushButton("←")
        before_button.clicked.connect(self.onBeforeButtonClicked)

        after_button = QtWidgets.QPushButton("→")
        after_button.clicked.connect(self.onAfterButtonClicked)

        self.path_lineedit = QtWidgets.QLineEdit()
        self.path_lineedit.returnPressed.connect(self.onPathLineEditReturnPressed)

        self.leftpanel_widget = leftpaneltabwidget.LeftPanelTabWidget()
        self.leftpanel_widget.place_list.list_view.doubleClicked.connect(
            self.onPlacesListClicked
        )

        self.file_list = filelist.FileList()
        self.file_list.doubleClicked.connect(self.onFileListClicked)

        # Add Widgets =========================================================
        topbar_layout.addWidget(before_button)
        topbar_layout.addWidget(after_button)
        topbar_layout.addWidget(self.path_lineedit)

        leftpanel_layout.addWidget(self.leftpanel_widget)

        file_layout.addWidget(self.file_list)

        # Add Layouts =========================================================
        central_layout.addLayout(leftpanel_layout, 1)
        central_layout.addLayout(file_layout, 4)

        top_layout.addLayout(topbar_layout)
        top_layout.addLayout(central_layout)

        self.setLayout(top_layout)

        # Other ===============================================================
        self.updateFileList()

    def updateFileList(self):
        self.file_list.item_model.removeRows(0, self.file_list.item_model.rowCount())
        path = os.path.join(current_path, "*")
        file_list = glob.glob(path)
        for file in file_list:
            filename = os.path.basename(file)
            if os.path.isfile(file):
                filesize = convertFileSize(os.path.getsize(file))
                item_type = "file"
            elif os.path.isdir(file):
                filesize = convertFileSize(getDirectorySize(file))
                item_type = "folder"
            file_modified_time_ = datetime.datetime.fromtimestamp(
                os.stat(file).st_mtime
            )
            file_modified_time = file_modified_time_.strftime("%Y/%m/%d %H:%M")

            list_row = list()
            item = IconAndFileNameItem(item_type)
            item.setText(filename)
            list_row.append(item)
            for info in [filesize, file_modified_time]:
                item = QtGui.QStandardItem()
                item.setText(info)
                list_row.append(item)
            self.file_list.item_model.appendRow(list_row)

        self.path_lineedit.setText(current_path)

    def moveDirectory(self):
        global current_path, current_moving_index
        if len(moving_history) > current_moving_index + 1:
            current_moving_index_ = current_moving_index + 1
            del moving_history[current_moving_index_:]
        moving_history.append(current_path)
        current_moving_index += 1
        self.updateFileList()

    def onPathLineEditReturnPressed(self):
        global current_path
        current_path = self.path_lineedit.text()
        self.moveDirectory()

    def onFileListClicked(self):
        global current_path
        row = self.file_list.selectedIndexes()[0].row()
        row_content = self.file_list.item_model.item(row, 0).text()
        filepath = os.path.join(current_path, row_content)

        if os.path.isfile(filepath):
            pass
        elif os.path.isdir(filepath):
            current_path = filepath
            self.moveDirectory()

    def onPlacesListClicked(self):
        global current_path
        row = self.leftpanel_widget.place_list.list_view.selectedIndexes()[0].row()
        current_path = os.path.expanduser(places_path_list[row])
        self.moveDirectory()

    def onBeforeButtonClicked(self):
        global current_path, current_moving_index
        if (len(moving_history) <= 1) or current_moving_index < 1:
            return
        current_moving_index -= 1
        current_path = moving_history[current_moving_index]
        self.updateFileList()

    def onAfterButtonClicked(self):
        global current_path, current_moving_index
        if len(moving_history) == current_moving_index + 1:
            return
        current_moving_index += 1
        current_path = moving_history[current_moving_index]
        self.updateFileList()


class IconAndFileNameItem(QtGui.QStandardItem):
    def __init__(self, type, parent=None):
        super(IconAndFileNameItem, self).__init__(parent)

        if type == "file":
            self.setIcon(QtGui.QIcon.fromTheme("text-x-generic"))
        elif type == "folder":
            self.setIcon(QtGui.QIcon.fromTheme("folder"))


def convertFileSize(size):
    units = ("B", "KiB", "MiB", "GiB", "TiB", "PiB")
    i = math.floor(math.log(size, 1024)) if size > 0 else 0
    size = round(size / 1024**i, 2)

    return f"{size}{units[i]}"


def getDirectorySize(path):
    total = 0
    try:
        for entry in os.scandir(path):
            if entry.is_file():
                total += entry.stat().st_size
    except PermissionError:
        pass
    return total


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
