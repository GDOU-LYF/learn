# これはサンプルの Python スクリプトです。

# Shift+F10 を押して実行するか、ご自身のコードに置き換えてください。
# Double Shift を押すと、クラス/ファイル/ツールウィンドウ/アクション/設定を検索します。


# def print_hi(name):
#     # スクリプトをデバッグするには以下のコード行でブレークポイントを使用してください。
#     print(f'Hi, {name}')  # Ctrl+F8を押すとブレークポイントを切り替えます。


import sys
from PyQt5 import QtWidgets, QtCore

# ガター内の緑色のボタンを押すとスクリプトを実行します。
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    widget.resize(360, 360)
    widget.setWindowTitle("hello,Pyqt5")
    widget.show()
    sys.exit(app.exec_())

# PyCharm のヘルプは https://www.jetbrains.com/help/pycharm/ を参照してください
