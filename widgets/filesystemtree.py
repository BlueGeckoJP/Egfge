from PySide6 import QtWidgets

import globalvalues


class FileSystemTree(QtWidgets.QTreeView):
    def __init__(self, *args, **kwargs):
        super(FileSystemTree, self).__init__(*args, **kwargs)

        gv = globalvalues.GlobalValues()

        self.item_model = QtWidgets.QFileSystemModel()
        self.item_model.setRootPath(gv.current_path)

        self.setModel(self.item_model)
        self.setRootIndex(self.item_model.index(gv.current_path))
