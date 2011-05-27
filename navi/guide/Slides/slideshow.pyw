#!/usr/bin/env python

"""
slideshow.pyw

A tool to show the slides for the Creating GUI Applications with PyQt and
Qt Designer talk at PyCon UK 2007.

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

import os, sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

this_dir = os.path.split(os.path.abspath(__file__))[0]
sys.path.append(os.path.join(this_dir, "Plugins", "widgets"))

from ui_slides import Ui_IntroductionToPyQt4


class PrintHelper(QObject):

    text_widgets = ("HighlightedTextEdit", "DisplayText") #, "QLabel", "QTextEdit")
    top_level_only = {
        "QLabel": True, "QTextEdit": True, "HighlightedTextEdit": False,
        "DisplayText": False, "SvgWidget": False
        }
    ignore = ()
    
    def __init__(self, widget):
    
        QObject.__init__(self)
        self.form = widget
        self.stackedWidget = widget.stackedWidget
        self.printer = QPrinter()
        self.printer.setPageSize(QPrinter.A4)
        self.printer.setOutputFormat(QPrinter.PdfFormat)
        self.printer.setPageOrder(QPrinter.FirstPageFirst)
        self.printer.setOrientation(QPrinter.Landscape)
        # Use the coordinate system for the whole paper, not just the
        # printable area.
        self.printer.setFontEmbeddingEnabled(True)
        self.printer.setOutputFileName("slides.pdf")
        
        quitAction = QAction(self.form)
        quitAction.setShortcut(QKeySequence("Ctrl+Q"))
        self.form.addAction(quitAction)
        
        fullScreenAction = QAction(self.form)
        fullScreenAction.setShortcut(QKeySequence("Ctrl+F"))
        self.form.addAction(fullScreenAction)
        
        printAction = QAction(self.form)
        printAction.setShortcut(QKeySequence("Ctrl+P"))
        self.form.addAction(printAction)
        
        previousAction = QAction(self.form)
        previousAction.setShortcut(QKeySequence("Left"))
        self.form.addAction(previousAction)
        
        nextAction = QAction(self.form)
        nextAction.setShortcut(QKeySequence("Right"))
        self.form.addAction(nextAction)
        
        self.indent = 0
        widget.counterLabel.setMaximum(self.stackedWidget.count())
        widget.counterLabel.setValue(1)
        self.stackedWidget.setCurrentIndex(0)
        
        self.connect(quitAction, SIGNAL("triggered(bool)"), qApp, SLOT("quit()"))
        self.connect(printAction, SIGNAL("triggered(bool)"), self.printSlides)
        self.connect(fullScreenAction, SIGNAL("triggered(bool)"), self.toggleFullScreen)
        self.connect(previousAction, SIGNAL("triggered(bool)"),
                     widget.previousButton, SLOT("click()"))
        self.connect(nextAction, SIGNAL("triggered(bool)"),
                     widget.nextButton, SLOT("click()"))
        self.connect(widget.printButton, SIGNAL("clicked()"), self.printSlides)
    
    def toggleFullScreen(self, enable):
    
        if self.form.isFullScreen():
            self.form.showNormal()
        else:
            self.form.showFullScreen()
    
    def printSlides(self):
    
        self.painter = QPainter()
        
        self.painter.begin(self.printer)
        self.painter.setRenderHint(QPainter.SmoothPixmapTransform)
        self.painter.setRenderHint(QPainter.Antialiasing)
        
        if self.stackedWidget.currentIndex() != 0:
            self.form.counterLabel.setValue(1)
        
        self.printPage(1)
        
    def printPage(self, index):
    
        qApp.processEvents()
        widget = self.stackedWidget.currentWidget()
        
        rect = self.printer.pageRect()
        x, y = self.printer.paperRect().x(), self.printer.paperRect().y()
        
        self.painter.save()
        xscale = float(rect.width())/widget.width()
        yscale = float(rect.height())/widget.height()
        scale = min(xscale, yscale)
        self.painter.translate(x + rect.width()/2, y + rect.height()/2)
        self.painter.scale(scale, scale)
        self.painter.translate(-widget.width()/2,
                               -widget.height()/2)
        
        self.printChildren(widget, QPoint(0, 0))
        
        self.painter.restore()
        
        if index + 1 > self.stackedWidget.count():
            self.stopPrinting()
        else:
            self.printer.newPage()
            self.form.counterLabel.setValue(index + 1)
            self.printPage(index + 1)
    
    def printChildren(self, widget, offset, in_text = False):
    
        for child in widget.children():
        
            if not isinstance(child, QWidget) or not child.isVisible() \
                or str(child.metaObject().className()) in self.ignore:
                continue
            
            text_widget = False
            painter_widget = False
            widget_name = str(child.metaObject().className())
            
            if widget_name == "QSvgWidget":
            
                painter_widget = True
            
            elif widget_name in self.text_widgets:
                if self.top_level_only[str(child.metaObject().className())]:
                    if self.stackedWidget.indexOf(child.parentWidget()) != -1:
                        text_widget = True
                else:
                    text_widget = True
            
            if widget_name == "QGLWidget":
            
                pixmap = child.renderPixmap(child.width(), child.height())
                self.painter.drawPixmap(offset + child.pos(), pixmap)
            
            elif text_widget or in_text:
            
                if child.autoFillBackground():
                    self.painter.fillRect(
                        QRect(offset + child.pos(), child.size()),
                        child.palette().color(QPalette.Window) # Base
                        )
                
                picture = QPicture()
                qApp.sendPostedEvents(child, 0)
                QPainter.setRedirected(child, picture)
                
                event = QPaintEvent(QRect(QPoint(0, 0), child.size()))
                qApp.sendEvent(child, event)
                QPainter.restoreRedirected(child)
                
                self.painter.drawPicture(offset + child.pos(), picture)
                self.printChildren(child, offset + child.pos(), in_text = True)
            
            else:
            
                w = child
                while not w.autoFillBackground():
                    if w.parentWidget():
                        w = w.parentWidget()
                    else:
                        break
                
                color = w.palette().color(QPalette.Window)
                
                image = QImage(child.size(), QImage.Format_RGB32)
                image.fill(qRgb(color.red(), color.green(), color.blue()))
                qApp.sendPostedEvents(child, 0)
                QPainter.setRedirected(child, image)
                
                event = QPaintEvent(QRect(QPoint(0, 0), child.size()))
                qApp.sendEvent(child, event)
                QPainter.restoreRedirected(child)
                
                self.painter.drawImage(offset + child.pos(), image)
                self.printChildren(child, offset + child.pos(), in_text = text_widget)
    
    def stopPrinting(self):
    
        self.painter.end()
        self.form.counterLabel.setValue(1)


class Form(QWidget, Ui_IntroductionToPyQt4):

    def __init__(self, parent = None):
    
        QWidget.__init__(self, parent)
        self.setupUi(self)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    form = Form()
    form.show()
    printHelper = PrintHelper(form)
    sys.exit(app.exec_())
