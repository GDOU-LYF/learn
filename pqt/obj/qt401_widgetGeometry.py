# -*- coding: utf-8 -*-

'''
    【简介】
     PyQt5中坐标系统

'''

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

app = QApplication(sys.argv)
widget = QWidget()
btn = QPushButton(widget)
btn.setText("Button")
# 以QWidget左上角为(0, 0)点
btn.move(20, 20)
# 不同操作系统可能对窗口最小宽度有规定，若设置宽度小于规定值，则会以规定值进行显示
widget.resize(300, 200)
# 以屏幕左上角为(0, 0)点
widget.move(250, 200)


def display():
    print("#1 QWidget")
    print("widget.(x,y)=({},{})".format(widget.x(), widget.y()))  # 获取窗口(含标题栏)到屏幕(0,0)的距离
    print("widget.(width,height)=({},{})".format(widget.width(), widget.height()))  # 获取客户区的宽度和高度

    print("#2 QWidget.geometry")  # 获取客户区信息
    print("widget.geometry().(x,y)=({},{})".format(widget.geometry().x(),
                                                   widget.geometry().y()))  # 获取客户区(不含标题栏)到屏幕(0,0)的距离
    print("widget.geometry().(width,height)=({},{})".format(widget.geometry().width(),
                                                            widget.geometry().height()))  # 获取客户区的宽度和高度
    print("widget.size().(width,height)=({},{})".format(widget.size().width(), widget.size().height()))  # 获取客户区的宽度和高度

    print("#3 QWidget.frameGeometry")  # 获取窗口信息
    print("widget.frameGeometry().(width,height)=({},{})".format(widget.frameGeometry().width(),
                                                                 widget.frameGeometry().height()))# 获取窗口(含边框的宽度)的宽度和高度
    print("widget.pos().(x,y)=({},{})".format(widget.pos().x(), widget.pos().y()))  # 获取窗口(含标题栏)到屏幕(0,0)的距离


btn.clicked.connect(display)
widget.setWindowTitle('PyQt坐标系统例子')
widget.show()

sys.exit(app.exec_())
