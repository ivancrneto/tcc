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
        self.grid = QHBoxLayout()
        self.centralwidget.setLayout(self.grid)
        self.addIcons()
        
        self.add_buttons_to_grid()
        self.connect(self.actionNew_Project, SIGNAL(_fromUtf8("triggered()")),
            self.new_project)
        self.connect(self.actionOpen_Project, SIGNAL(_fromUtf8("triggered()")),
            self.open_project)
        self.connect(self.actionSave_Project, SIGNAL(_fromUtf8("triggered()")),
            self.save_project)
        #self.connect(self.actionDatabase, SIGNAL(_fromUtf8("triggered()")),
        #    self.add_buttons_to_grid)
        #temporarily
        self.move(500, 400)
        
    
    def addIcons(self):
        #new_project action
        self.actionNew_Project = QAction(
            QIcon(os.path.join(os.path.dirname(__file__), 'icons/newproject.png')), 'New Project', self)
        self.actionOpen_Project = QAction(
            QIcon(os.path.join(os.path.dirname(__file__), 'icons/openproject.png')), 'Open Project', self)
        self.actionSave_Project = QAction(
            QIcon(os.path.join(os.path.dirname(__file__), 'icons/saveproject.png')), 'Save Project', self)
        #self.actionDatabase = QAction(
        #    QIcon(os.path.join(os.path.dirname(__file__), 'icons/database.png')), 'Database', self)
        
        #self.actionSave_Project.setDisabled(True)
        #self.actionDatabase.setDisabled(True)
        
        self.toolbar = self.addToolBar('Toolbar')
        self.toolbar.addAction(self.actionNew_Project)
        self.toolbar.addAction(self.actionOpen_Project)
        self.toolbar.addAction(self.actionSave_Project)
        self.toolbar.addSeparator()
        #self.toolbar.addAction(self.actionDatabase)
    
    def clean_grid(self):
        while self.grid.count() > 0:
            item = self.grid.takeAt(self.grid.count() - 1)
            self.grid.removeItem(item)
        
        self.grid.update()
        self.grid.activate()
        
    def add_buttons_to_grid(self):
        if not hasattr(self, 'project'):
            self.project_button_grid()
            return
        if self.project.state in (None, 'new', 'similarity_matrix'):
            self.project_button_grid()
        if self.project.state in ('new', 'similarity_matrix'):
            self.database_button_grid()
            
        #self.actionSave_Project.setEnabled(True)
    
    def add_arrow_grid(self):
        image = QPixmap(os.path.join(os.path.dirname(__file__), 'icons/arrow.png'))
        label = QLabel(self)
        label.setPixmap(image)
        self.grid.insertWidget(self.grid.count() - 1, label, 0)
    
    def project_button_grid(self):
        qtool_button = QToolButton(self)
        qtool_button.setIcon(QIcon(os.path.join(os.path.dirname(__file__), 'icons/folder_open.png')))
        qtool_button.setIconSize(QSize(48, 48))
        self.grid.addWidget(qtool_button, 0)
        spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.grid.addItem(spacer)
    
    def database_button_grid(self):
        self.add_arrow_grid()
        
        qtool_button = QToolButton(self)
        qtool_button.setIcon(QIcon(os.path.join(os.path.dirname(__file__), 'icons/database-big.png')))
        qtool_button.setIconSize(QSize(48, 48))
        self.grid.insertWidget(self.grid.count() - 1, qtool_button, 0)
        
        self.connect(qtool_button, SIGNAL(_fromUtf8("clicked()")),
            self.choose_sequences)
    
    def new_project(self):
        project_dialog = NewProject(self)
        project_dialog.exec_()
        if project_dialog.accepted:
            if hasattr(self, 'project') and self.project != None:
                self.project.end()
            self.clean_grid()
            self.project = Project(project_dialog.project_name.text(),
                project_dialog.project_path.text(), project_dialog.database_path.text())
            #self.actionDatabase.setEnabled(True)
            self.add_buttons_to_grid()
            
    def choose_sequences(self):
        sequences_map = self.project.get_sequences()
        choose_sequences_dialog = ChooseSequences(sequences_map, self)
        choose_sequences_dialog.exec_()
        if choose_sequences_dialog.accepted:
            selected_sequences = choose_sequences_dialog.selected_sequences()
            if selected_sequences:
                done = self.project.generate_similarities(selected_sequences)
                if done:
                    self.project.save_project()
            
    def open_project(self):
        self.clean_grid()
        if hasattr(self, 'project') and self.project != None:
            self.project.end()
        project_path = QFileDialog.getOpenFileName(self, 'Open Project', os.path.expanduser('~'), "Navi Project Files (*.nav)")
        #TODO: it is better if we override __new__ method in Project class instead of pass None args
        if project_path not in (None, ''):
            self.project = Project(None, project_path, None)
            self.project = self.project.load_data()
            self.add_buttons_to_grid()
        
    def save_project(self):
        if hasattr(self, 'project'):
            self.project.save_project()
