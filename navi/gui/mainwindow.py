from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui_mainwindow import Ui_MainWindow
from base.makecoba import Makecoba

try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent = None):

        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.makecoba = Makecoba()
        self.connect(self.actionNew_Project, SIGNAL(_fromUtf8("triggered()")),
            self.new_project)
        
    def new_project(self):
        self.file_dialog = QFileDialog(self)
        self.file_dialog.setAcceptMode(QFileDialog.AcceptOpen)
        self.file_dialog.setFileMode(QFileDialog.Directory)
        self.file_dialog.getOpenFileName(self, 'Open File', '/home')
        #self.makecoba.new_project('Ivan')
