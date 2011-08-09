from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui.mainwindow import Ui_MainWindow
from dialogs import NewProject
from base.makecoba import Project
import os


try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class MainWindow(QMainWindow, Ui_MainWindow):
    '''
    Class for the main window of the software
    '''
    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.setWindowTitle('Navi')
        self.addIcons()
        #screen = QDesktopWidget().screenGeometry()
        #self.resize(screen.width(), screen.height())
        #self.makecoba = Makecoba()
        self.connect(self.actionNew_Project, SIGNAL(_fromUtf8("triggered()")),
            self.new_project)
        #temporarily
        self.move(500, 500)
    
    def addIcons(self):
        #new_project action
        self.actionNew_Project = QAction(
            QIcon(os.path.join(os.path.dirname(__file__), 'icons/fileopen.png')), 'New Project', self)
        
        self.toolbar = self.addToolBar('New Project')
        self.toolbar.addAction(self.actionNew_Project)
    
    def new_project(self):
        project_dialog = NewProject(self)
        project_dialog.exec_()
        if project_dialog.accepted:
            print 'accepted'
            project = Project(project_dialog.project_name.text(), project_dialog.project_path.text())
            project.save_file('w')
        else:
            print 'not accepted'
        #new_project.close()
        #file_name = QFileDialog.getSaveFileName(self, 'Save Project File',
        #    os.path.expanduser('~'), 'Navi Project file (*.nav)')
        #makecoba = Makecoba()
        #makecoba.new_project(file_name)
        
