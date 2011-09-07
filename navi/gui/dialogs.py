from PyQt4.QtGui import *
from PyQt4.QtCore import *
from ui.new_project import Ui_NewProject
import os

class NewProject(QDialog, Ui_NewProject):
    '''
    Class with a dialog to the user fill the
    data for a new project
    '''
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.setModal(True)
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.connect(self.browse_project_button, SIGNAL('clicked()'), self.browse_project_directory)
        self.connect(self.browse_database_button, SIGNAL('clicked()'), self.browse_database_directory)
        #self.move((screen.width() - size.width())/2,
        #          (screen.height() - size.height())/2)
    
    def accept(self):
        if self.project_name.text() and self.project_path.text() and self.database_path.text():
            self.accepted = True
        self.close()
    
    def reject(self):
        self.accepted = False
        self.close()
        
    def closeEvent(self, event):
        self.emit(SIGNAL("closed()"))
        
    #TODO: change to become only one function
    def browse_project_directory(self):
        self.project_path.setText(QFileDialog.getExistingDirectory(self, 'Choose the directory',
            os.path.expanduser('~')))
            
    def browse_database_directory(self):
        self.database_path.setText(QFileDialog.getExistingDirectory(self, 'Choose the directory',
            os.path.expanduser('~')))
            
            
class ChooseSequences(QDialog, Ui_ChooseSequences):
    '''
    Class with a dialog to the user choose the sequences to generate
    the similarity matrix
    '''
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.setModal(True)
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        #self.move((screen.width() - size.width())/2,
        #          (screen.height() - size.height())/2)
    
    def accept(self):
        print 'choose sequences accepted'
        self.accepted = True
        self.close()
    
    def reject(self):
        print 'choose sequences rejected'
        self.accepted = False
        self.close()
        
    def closeEvent(self, event):
        self.emit(SIGNAL("closed()"))
    
    
    
    
    
    
