from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui.mainwindow import Ui_MainWindow
from dialogs import NewProject, ChooseSequences
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
        self.grid = QGridLayout()
        self.centralwidget.setLayout(self.grid)
        self.addIcons()
        #screen = QDesktopWidget().screenGeometry()
        #self.resize(screen.width(), screen.height())
        #self.makecoba = Makecoba()
        self.addButtonToGrid()
        self.connect(self.actionNew_Project, SIGNAL(_fromUtf8("triggered()")),
            self.new_project)
        self.connect(self.actionOpen_Project, SIGNAL(_fromUtf8("triggered()")),
            self.open_project)
        self.connect(self.actionSave_Project, SIGNAL(_fromUtf8("triggered()")),
            self.save_project)
        self.connect(self.actionDatabase, SIGNAL(_fromUtf8("triggered()")),
            self.database_button)
        #temporarily
        self.move(500, 500)
    
    def addIcons(self):
        #new_project action
        self.actionNew_Project = QAction(
            QIcon(os.path.join(os.path.dirname(__file__), 'icons/newproject.png')), 'New Project', self)
        self.actionOpen_Project = QAction(
            QIcon(os.path.join(os.path.dirname(__file__), 'icons/openproject.png')), 'Open Project', self)
        self.actionSave_Project = QAction(
            QIcon(os.path.join(os.path.dirname(__file__), 'icons/saveproject.png')), 'Save Project', self)
        self.actionDatabase = QAction(
            QIcon(os.path.join(os.path.dirname(__file__), 'icons/database.png')), 'Database', self)
        
        self.actionSave_Project.setDisabled(True)
        self.actionDatabase.setDisabled(True)
        
        self.toolbar = self.addToolBar('Toolbar')
        self.toolbar.addAction(self.actionNew_Project)
        self.toolbar.addAction(self.actionOpen_Project)
        self.toolbar.addAction(self.actionSave_Project)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.actionDatabase)
        
    def addButtonToGrid(self):
        qtool_button = QToolButton(self)
        qtool_button.setIcon(QIcon(os.path.join(os.path.dirname(__file__), 'icons/folder_open.png')))
        qtool_button.setIconSize(QSize(48, 48))
        self.grid.addWidget(qtool_button, 0, 1)
        
        image = QPixmap(os.path.join(os.path.dirname(__file__), 'icons/arrow.png'))
        label = QLabel(self)
        label.setPixmap(image)
        self.grid.addWidget(label, 0, 2)
    
    def database_button(self):
        qtool_button = QToolButton(self)
        qtool_button.setIcon(QIcon(os.path.join(os.path.dirname(__file__), 'icons/database-big.png')))
        qtool_button.setIconSize(QSize(48, 48))
        self.grid.addWidget(qtool_button, 0, 3)
        self.connect(qtool_button, SIGNAL(_fromUtf8("clicked()")),
            self.choose_sequences)
    
    def new_project(self):
        project_dialog = NewProject(self)
        project_dialog.exec_()
        if project_dialog.accepted:
            if hasattr(self, 'project') and self.project != None:
                self.project.end()
            self.project = Project(project_dialog.project_name.text(),
                project_dialog.project_path.text(), project_dialog.database_path.text())
            self.actionDatabase.setEnabled(True)
            
    def choose_sequences(self):
        choose_sequences_dialog = ChooseSequences(self)
        choose_sequences_dialog.exec_()
            
    def open_project(self):
        print 'implement open project'
        
    def save_project(self):
        print 'implement save project'
