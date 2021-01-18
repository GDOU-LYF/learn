# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog

from children import Ui_ChildrenForm
from children2 import Ui_childrenForm2


class MainWindow(QMainWindow, Ui_ChildrenForm):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        # event
        self.fileCloseAction.triggered.connect(self.close)
        self.fileOpenAction.triggered.connect(self.openMsg)

        # children
        self.child = ChildrenForm()  # 创建一个新类
        self.MaingridLayout.addWidget(self.child)  # 将组件添加到LayOut布局
        self.child.show()

    def openMsg(self):
        file, ok = QFileDialog.getOpenFileName(self, "打开", "C:/", "All Files(*);;Text Files(*.txt)")
        print(file)
        self.statusbar.showMessage(file)


class ChildrenForm(QMainWindow, Ui_childrenForm2):  # 注意继承
    def __init__(self, parent=None):
        super(ChildrenForm, self).__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MainWindow()
    myWin.show()
    sys.exit(app.exec_())
