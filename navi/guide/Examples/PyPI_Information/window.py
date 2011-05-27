"""
window.py

The window for the PyPI Information example application.

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

from PyQt4.QtCore import Qt, SIGNAL
from PyQt4.QtGui import *

from ui_window import Ui_Window
import pypi

class Window(QWidget, Ui_Window):

    terms = [ "name", "version", "author", "author_email",
              "maintainer", "maintainer_email", "home_page", "license",
              "summary", "description", "keywords", "platform",
              "download_url" ]
    
    def __init__(self, parent = None):
    
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.connect(self.searchButton, SIGNAL("clicked()"),
                     self.search)
    
    def search(self):
    
        self.treeWidget.clear()
        
        qApp.setOverrideCursor(Qt.WaitCursor)
        
        server = pypi.PackageServer("http://pypi.python.org/pypi")
        matches = server.search(
            { unicode(self.terms[self.fieldCombo.currentIndex()]):
              unicode(self.termsEdit.text()) }, "and" )
        
        qApp.restoreOverrideCursor()
        
        if len(matches) == 0:
            QMessageBox.information(self, self.tr("PyPI Information"),
                                    self.tr("No results found."))
            return
        
        for match in matches:
        
            item = QTreeWidgetItem()
            if not match["name"]:
                continue
            
            item.setText(0, match["name"])
            if match["summary"]:
                item.setText(1, match["summary"])
            
            self.treeWidget.addTopLevelItem(item)
