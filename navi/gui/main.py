#!/usr/bin/env python

from PyQt4 import QtGui
from mainwindow import MainWindow
import sys

__version__ = "1.0"


def init():

    app = QtGui.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    init()
