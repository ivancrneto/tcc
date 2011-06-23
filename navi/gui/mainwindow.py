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
        #self.file_dialog = QFileDialog(self)
        #self.file_dialog.setAcceptMode(QFileDialog.AcceptSave)
        #self.file_dialog.setFileMode(QFileDialog.AnyFile)
        import os

        a = QFileDialog.getSaveFileNameAndFilter(self,
            'Save Project File', os.path.expanduser('~'), 
            'Navi Project file (*.nav)')
        print a
        #self.file_dialog = QFileDialog(self)
        #self.file_dialog.setAcceptMode(QFileDialog.AcceptSave)
        #self.file_dialog.setFileMode(QFileDialog.AnyFile)
        #self.file_dialog.setDirectory(os.path.expanduser('~'))
        #self.file_dialog.setNameFilter('Navi Project file (*.nav)')
        #self.file_dialog.open()        
        #a = self.file_dialog.selectedFiles()
        #print a.last()
        #file_name = getSaveFileNameAndFilter(None, 'Choose the file name', '/home', QString filter = QString(), QString initialFilter = QString(), Options options = 0)
