"""
mainwindow.py

The main window for the Logo Maker example application.

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

from PyQt4.QtCore import pyqtSignature, QString, Qt, QVariant, SIGNAL, SLOT
from PyQt4.QtGui import *
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent = None):
    
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        
        self.fontDatabase = QFontDatabase()
        self.path = QString()
        
        self.connect(self.exitAction, SIGNAL("triggered()"),
                     qApp, SLOT("quit()"))
        
        self.updateStylesCombo(self.fontComboBox.currentFont().family())
        self.setWindowModified(False)
    
    @pyqtSignature("")
    def on_newAction_triggered(self):
    
        self.effectWidget.reset()
        self.setWindowModified(False)
        self.saveAsAction.setEnabled(False)
        self.saveAction.setEnabled(False)
    
    def on_fontComboBox_currentFontChanged(self, font):
    
        self.updateStylesCombo(font.family())
        
    def updateStylesCombo(self, family):
    
        self.styleComboBox.clear()
        
        styles = self.fontDatabase.styles(family)
        for style in styles:
        
            self.styleComboBox.addItem(style)
    
    @pyqtSignature("")
    def on_saveAsAction_triggered(self):
    
        filters = self.tr("Supported formats (%1)").arg(
            " ".join(map(lambda x: "*."+str(x), QImageWriter.supportedImageFormats()))
            )
        path = QFileDialog.getSaveFileName(self, self.tr("Save Image"),
            self.path, filters)
        
        if path.isEmpty():
            return
        
        self.save(path)
    
    @pyqtSignature("")
    def on_saveAction_triggered(self):
    
        self.save(self.path)
    
    def save(self, path):
    
        rect = self.effectWidget.pathRect()
        image = QImage(rect.size().toSize(), QImage.Format_ARGB32)
        image.fill(qRgba(0, 0, 0, 0))
        self.effectWidget.paint(image, rect)
        if image.save(path):
            self.setWindowModified(False)
            self.saveAction.setEnabled(False)
            self.path = path
    
    def on_effectWidget_contentsChanged(self):
    
        self.setWindowModified(True)
        self.saveAsAction.setEnabled(True)
        self.saveAction.setEnabled(not self.path.isEmpty())
