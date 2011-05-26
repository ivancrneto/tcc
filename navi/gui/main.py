#!/usr/bin/env python

from PyQt4 import QtGui, QtCore
from mainwindow import Ui_MainWindow
import sys

#class MainWindow(Ui_MainWindow):
#    def __init__(self):
#        self.mainwindow = QtGui.QMainWindow()
#        Ui_MainWindow.setupUi(self, self.mainwindow)
#        
#    def show(self):
#        self.mainwindow.show()

class MainWindow(Ui_MainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
#        ui = Ui_MainWindow()
#        ui.setupUi(self)
        
    #def show(self):
    #    self.mainwindow.show()

def init():
    app = QtGui.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    init()
