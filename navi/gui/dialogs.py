from PyQt4.QtGui import *
from ui.new_project import Ui_NewProject

class NewProject(QDialog, Ui_NewProject):
    '''
    Class with a dialog to the user fill the
    data for a new project
    '''
    def __init__(self, parent = None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width())/2,
                  (screen.height() - size.height())/2)
                  
    def accept(self):
        print 'accepted'
        print self.project_name.text()
        print self.project_path.text()
        
    def reject(self):
        print 'rejected'
