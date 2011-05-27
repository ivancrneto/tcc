#!/usr/bin/env python

"""
displaytextplugin.py

A display text custom widget plugin for Qt Designer.

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

from PyQt4 import QtCore, QtGui, QtDesigner
from displaytext import DisplayText


def Q_TYPEID(class_name):

    return QtCore.QString("com.trolltech.Qt.Designer.TaskMenu")


class DisplayTextPlugin(QtDesigner.QPyDesignerCustomWidgetPlugin):

    def __init__(self, parent = None):
    
        QtDesigner.QPyDesignerCustomWidgetPlugin.__init__(self)

        self.initialized = False

    def initialize(self, formEditor):

        if self.initialized:
            return
        
        manager = formEditor.extensionManager()
        if manager:
            self.factory = DisplayTextTaskMenuFactory(manager)
            manager.registerExtensions(
                self.factory, Q_TYPEID("QDesignerTaskMenuExtension")
                )
        
        self.initialized = True

    def isInitialized(self):

        return self.initialized

    def createWidget(self, parent):

        widget = DisplayText(parent)
        widget.setText("Display Text")
        return widget

    def name(self):

        return "DisplayText"

    def group(self):

        return "PyQt Examples"

    def icon(self):

        return QtGui.QIcon()

    def toolTip(self):

        return ""

    def whatsThis(self):

        return ""

    def isContainer(self):

        return False

    def domXml(self):

        return (
               '<widget class="%s" name=\"displayText\" />\n'
               ) % "DisplayText"

    def includeFile(self):

        return "displaytext"


class DisplayTextTaskMenuFactory(QtDesigner.QExtensionFactory):

    def __init__(self, parent = None):
    
        QtDesigner.QExtensionFactory.__init__(self, parent)
    
    def createExtension(self, obj, iid, parent):
    
        if iid != Q_TYPEID("QPyDesignerTaskMenuExtension"):
            return None
        
        if isinstance(obj, DisplayText):
            return DisplayTextTaskMenu(obj, parent)
        
        return None


class DisplayTextTaskMenu(QtDesigner.QPyDesignerTaskMenuExtension):

    def __init__(self, textEdit, parent):
    
        QtDesigner.QPyDesignerTaskMenuExtension.__init__(self, parent)
        
        self.textEdit = textEdit
        
        self.editStateAction = QtGui.QAction("Edit Text...", self)
        self.connect(self.editStateAction, QtCore.SIGNAL("triggered()"),
                     self.editText)
    
    def preferredEditAction(self):
    
        return self.editStateAction
    
    def taskActions(self):
    
        return [self.editStateAction]
    
    @QtCore.pyqtSignature("editText()")
    def editText(self):
    
        dialog = DisplayTextDialog(self.textEdit)
        dialog.exec_()


class DisplayTextDialog(QtGui.QDialog):

    def __init__(self, editor, parent = None):
    
        QtGui.QDialog.__init__(self, parent)
        
        self.editor = editor
        self.textEdit = QtGui.QTextEdit()
        self.textEdit.setHtml(editor.getText())
        
        okButton = QtGui.QPushButton("&OK")
        cancelButton = QtGui.QPushButton("&Cancel")
        
        self.connect(okButton, QtCore.SIGNAL("clicked()"), self.updateText)
        self.connect(cancelButton, QtCore.SIGNAL("clicked()"),
                     self, QtCore.SLOT("reject()"))
        
        buttonLayout = QtGui.QHBoxLayout()
        buttonLayout.addStretch(1)
        buttonLayout.addWidget(okButton)
        buttonLayout.addWidget(cancelButton)
        
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addLayout(buttonLayout)
        self.setLayout(layout)
    
    def updateText(self):
    
        formWindow = QtDesigner.QDesignerFormWindowInterface.findFormWindow(self.editor)
        if formWindow:
            formWindow.cursor().setProperty("text", QtCore.QVariant(self.textEdit.toHtml()))
        
        self.accept()
