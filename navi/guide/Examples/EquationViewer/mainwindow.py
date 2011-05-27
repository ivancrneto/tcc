"""
mainwindow.py

The main window for the Equation Viewer example application.

Copyright (C) 2007 David Boddie <david@boddie.org.uk>

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtNetwork import *
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent = None):
    
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        
        self.path = QString()
        self.mathSize = 3
        self.http = QHttp()
        self.connect(self.http, SIGNAL("done(bool)"), self.updateForm)
        
        self.connect(self.exitAction, SIGNAL("triggered()"), qApp, SLOT("quit()"))
        self.connect(self.aboutQtAction, SIGNAL("triggered()"), qApp, SLOT("aboutQt()"))
    
    @pyqtSignature("")
    def on_newAction_triggered(self):
    
        self.outputLabel.setPixmap(QPixmap())
        self.equationEditor.clear()
        self.path = QString()
        self.setWindowModified(False)
        self.saveAction.setEnabled(False)
    
    @pyqtSignature("")
    def on_updateAction_triggered(self):
    
        self.fetchImage()
    
    def fetchImage(self):
    
        self.newAction.setEnabled(False)
        self.updateAction.setEnabled(False)
        self.increaseMathAction.setEnabled(False)
        self.decreaseMathAction.setEnabled(False)
        self.equationEditor.setReadOnly(True)
        
        url = QUrl()
        url.setPath("/cgi-bin/mathtran")
        url.setQueryDelimiters("=", ";")
        url.addQueryItem("D", str(self.mathSize))
        url.addQueryItem("tex", str(QUrl.toPercentEncoding(
                         self.equationEditor.toPlainText())))
        
        self.http.setHost("mathtran.org")
        self.http.get(url.toString())
        self.statusBar().showMessage(self.tr("Fetching image..."))
    
    def updateForm(self, error):
    
        self.newAction.setEnabled(True)
        self.updateAction.setEnabled(True)
        self.increaseMathAction.setEnabled(True)
        self.decreaseMathAction.setEnabled(True)
        self.equationEditor.setReadOnly(False)
        self.statusBar().clearMessage()
        
        if error:
            return
        
        image = QImage()
        if not image.loadFromData(self.http.readAll()):
            return
        
        pixmap = QPixmap.fromImage(image)
        self.outputLabel.setPixmap(pixmap)
        self.statusBar().clearMessage()
        self.setWindowModified(True)
        self.saveAsAction.setEnabled(True)
        self.saveAction.setEnabled(not self.path.isEmpty())
    
    @pyqtSignature("")
    def on_saveAsAction_triggered(self):
    
        filters = self.tr("Supported formats (%1)").arg(
            " ".join(map(lambda x: "*."+str(x), QImageWriter.supportedImageFormats()))
            )
        path = QFileDialog.getSaveFileName(self, self.tr("Save Image As"),
            self.path, filters)
        
        if path.isEmpty():
            return
        
        self.save(path)
    
    def save(self, path = None):
    
        if not path:
            if self.path:
                path = self.path
            else:
                self.saveAs()
        
        if self.outputLabel.pixmap().save(path):
            self.setWindowModified(False)
            self.saveAction.setEnabled(True)
            self.path = path
    
    @pyqtSignature("")
    def on_increaseMathAction_triggered(self):
    
        self.mathSize = min(self.mathSize + 1, 10)
        self.fetchImage()
    
    @pyqtSignature("")
    def on_decreaseMathAction_triggered(self):
    
        self.mathSize = max(self.mathSize - 1, 1)
        self.fetchImage()
    
    @pyqtSignature("")
    def on_aboutAction_triggered(self):
    
        QMessageBox.about(self, self.tr("About MathTran Equation Viewer"),
            self.tr("<qt><h3>About MathTran Equation Viewer</h3>"
                    "<p>This application uses the MathTran Web service at "
                    '<a href="http://www.mathtran.org/">mathtran.org</a> to '
                    "let you preview equations written in TeX.</p></qt>"))
