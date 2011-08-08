from PyQt4.QtGui import *
from PyQt4.QtCore import *
from ui.new_project import Ui_NewProject

class NewProject(QDialog, Ui_NewProject):
    '''
    Class with a dialog to the user fill the
    data for a new project
    '''
    def __init__(self, parent = None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.setModal(True)
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        #self.move((screen.width() - size.width())/2,
        #          (screen.height() - size.height())/2)
    
    def accept(self):
        self.accepted = True
        self.close()
    
    def reject(self):
        self.accepted = False
        self.close()
        
    def closeEvent(self, event):
        self.emit(SIGNAL("closed()"))
    #def on_buttonBox_clicked(self):
    #    self.close()
        
    #def on_rejectButton_clicked(self):
    #    self.close()
