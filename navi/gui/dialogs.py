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
        self.connect(self.browse_button, SIGNAL('clicked()'), self.browse_directory)
        #self.move((screen.width() - size.width())/2,
        #          (screen.height() - size.height())/2)
    
    def accept(self):
        if self.project_name.text() and self.project_path.text():
            self.accepted = True
        self.close()
    
    def reject(self):
        self.accepted = False
        self.close()
        
    def closeEvent(self, event):
        self.emit(SIGNAL("closed()"))
        
    def browse_directory(self):
        self.project_path.setText(QFileDialog.getExistingDirectory(self, 'Choose the directory',
            os.path.expanduser('~')))
