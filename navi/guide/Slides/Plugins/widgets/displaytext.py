#!/usr/bin/env python

"""
displaytext.py

A PyQt custom widget example for Qt Designer.

Copyright (C) 2006 David Boddie <david@boddie.org.uk>
Copyright (C) 2005-2006 Trolltech ASA. All rights reserved.

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

from PyQt4 import QtCore, QtGui


class DisplayText(QtGui.QWidget):

    def __init__(self, parent = None):
    
        QtGui.QWidget.__init__(self, parent)
        self.setAutoFillBackground(False)
        
        self.label = QtGui.QLabel()
        
        layout = QtGui.QVBoxLayout()
        layout.setMargin(0)
        layout.addWidget(self.label)
        self.setLayout(layout)
        
        self.setAttribute(QtCore.Qt.WA_Hover)
    
    def getAlignment(self):
        return self.label.alignment()
    
    def setAlignment(self, value):
        self.label.setAlignment(value)
    
    alignment = QtCore.pyqtProperty("Qt::Alignment", getAlignment, setAlignment)
    
    def getIndent(self):
        return self.label.indent()
    
    def setIndent(self, value):
        self.label.setIndent(value)
    
    indent = QtCore.pyqtProperty("int", getIndent, setIndent)
    
    def getMargin(self):
        return self.label.margin()
    
    def setMargin(self, value):
        self.label.setMargin(value)
    
    margin = QtCore.pyqtProperty("int", getMargin, setMargin)
    
    def getText(self):
        return self.label.text()
    
    @QtCore.pyqtSignature("setText(const QString &)")
    def setText(self, text):
        self.label.setText(text)
    
    text = QtCore.pyqtProperty("QString", getText, setText)
    
    def getTextFormat(self):
        return self.label.textFormat()
    
    def setTextFormat(self, value):
        self.label.setTextFormat(value)
    
    textFormat = QtCore.pyqtProperty("Qt::TextFormat", getTextFormat, setTextFormat)
    
    def getWordWrap(self):
        return self.label.wordWrap()
    
    def setWordWrap(self, enable):
        self.label.setWordWrap(enable)
    
    wordWrap = QtCore.pyqtProperty("bool", getWordWrap, setWordWrap)
    
    # Slots
    
    @QtCore.pyqtSignature("clear()")
    def clear(self):
        self.label.clear()
    
    @QtCore.pyqtSignature("setMovie(QMovie *)")
    def setMovie(self, movie):
        self.label.setMovie(movie)
    
    @QtCore.pyqtSignature("setNum(int)")
    def setNum(self, number):
        self.label.setNum(number)
    
    @QtCore.pyqtSignature("setNum(double)")
    def setNum(self, number):
        self.label.setNum(number)
    
    @QtCore.pyqtSignature("setPicture(const QPicture &)")
    def setPicture(self, picture):
        self.label.setPicture(picture)
    
    @QtCore.pyqtSignature("setPixmap(const QPixmap &)")
    def setPixmap(self, pixmap):
        self.label.setPixmap(pixmap)


if __name__ == "__main__":

    import sys
    app = QtGui.QApplication(sys.argv)
    widget = DisplayText()
    widget.show()
    sys.exit(app.exec_())
