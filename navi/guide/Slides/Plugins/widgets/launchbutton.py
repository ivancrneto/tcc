#!/usr/bin/env python

"""
launchbuttonplugin.py

A custom widget plugin for Qt Designer.

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


class LaunchButton(QtGui.QPushButton):

    """LaunchButton(QtGui.QPushButton)
    
    Provides a push button that launches the executable specified in its path
    property when clicked.
    """
    
    def __init__(self, parent = None):
    
        QtGui.QPushButton.__init__(self, parent)
        
        self._path = QtCore.QString()
        
        self.connect(self, QtCore.SIGNAL("clicked()"), self.launch)
    
    # The path property holds the path to the executable that will be
    # launched when the button is clicked. We implement it using the
    # getPath() and setPath() methods.
    
    def getPath(self):
        return self._path
    
    def setPath(self, path):
        self._path = path
    
    path = QtCore.pyqtProperty("QString", getPath, setPath)
    
    def launch(self):
    
        if not self._path.isEmpty():
            QtCore.QProcess.startDetached(
                QtCore.QString("\"%1\"").arg(self._path))


if __name__ == "__main__":

    import sys
    app = QtGui.QApplication(sys.argv)
    widget = LaunchButton()
    widget.setText(QtCore.QString("Launch"))
    widget.setPath(QtCore.QString("designer"))
    widget.show()
    sys.exit(app.exec_())
