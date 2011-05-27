"""
effectwidget.py

An effect widget that enables the user to apply effects to a text label.

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

import random
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class EffectWidget(QWidget):

    __pyqtSignals__ = ("contentsChanged()",)
    
    def __init__(self, parent = None):
    
        QWidget.__init__(self, parent)
        self.fontDatabase = QFontDatabase()
        random.seed()
        self.reset()
    
    @pyqtSignature("")
    def reset(self):
    
        self._effects = (self.paintBackground, self.paintShadow,
                        self.paintFill, self.paintLines, self.paintOutline)
        self._enabledEffects = {self.paintOutline: Qt.DashLine}
        
        self._path = QPainterPath()
        self._font = QFont()
        self._font.setPointSizeF(64.0)
        self._fontFamily = self._font.family()
        self._fontStyle = ""
        self._fontSize = self._font.pointSizeF()
        self._text = ""
        self._background = Qt.white
        self._shadow = 3
        self._shadowColor = Qt.black
        self._fillColor = Qt.blue
        self._linesColor = Qt.green
        self._lines = 100
        self.updatePath()
    
    def paintEvent(self, event):
    
        self.paint(self, event.rect())
    
    def paint(self, device, rect):
    
        path = self._path
        pathRect = path.boundingRect()
        
        if path.isEmpty():
            return
        
        painter = QPainter()
        painter.begin(device)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.translate(device.width()/2, device.height()/2)
        painter.translate(-pathRect.center())
        
        for effect in self._effects:
        
            if self._enabledEffects.has_key(effect):
                effect(painter, path)
        
        painter.end()
    
    def sizeHint(self):
    
        return QSize(100, 100)
    
    def pathRect(self):
    
        pathRect = self._path.boundingRect()
        if not pathRect.isEmpty():
            pathRect.adjust(-16, -16, 16, 16)
        return pathRect
    
    def font(self):
    
        return self._font
    
    @pyqtSignature("QFont")
    def setFont(self, font):
    
        self._font = QFont(font)
        self.updatePath()
    
    font = pyqtProperty("QFont", font, setFont)
    
    @pyqtSignature("QFont")
    def setFontFamily(self, font):
    
        self._fontFamily = font.family()
        self._font = self.fontDatabase.font(
            self._fontFamily, self._fontStyle, self._fontSize
            )
        self.updatePath()
    
    @pyqtSignature("QString")
    def setFontStyle(self, style):
    
        self._fontStyle = unicode(style)
        self._font = self.fontDatabase.font(
            self._fontFamily, self._fontStyle, self._fontSize
            )
        self.updatePath()
    
    @pyqtSignature("double")
    def setFontSize(self, size):
    
        self._fontSize = size
        self._font = self.fontDatabase.font(
            self._fontFamily, self._fontStyle, self._fontSize
            )
        self.updatePath()
    
    def text(self):
    
        return self._text
    
    @pyqtSignature("QString")
    def setText(self, text):
    
        self._text = unicode(text)
        self.updatePath()
    
    text = pyqtProperty("QString", text, setText)
    
    def updatePath(self):
    
        self._path = QPainterPath()
        self._path.addText(0, 0, self._font, self._text)
        self.emit(SIGNAL("contentsChanged()"))
        self.update()
    
    def background(self):
        return self._background
    
    @pyqtSignature("QColor")
    def setBackground(self, value):
        self._background = value
        self.emit(SIGNAL("contentsChanged()"))
        self.update()
    
    background = pyqtProperty("QColor", background, setBackground)
    
    def shadow(self):
        return self._shadow
    
    @pyqtSignature("int")
    def setShadow(self, value):
        self._shadow = value
        self.emit(SIGNAL("contentsChanged()"))
        self.update()
    
    shadow = pyqtProperty("int", shadow, setShadow)
    
    def shadowColor(self):
        return self._shadowColor
    
    @pyqtSignature("QColor")
    def setShadowColor(self, value):
        self._shadowColor = value
        self.emit(SIGNAL("contentsChanged()"))
        self.update()
    
    shadowColor = pyqtProperty("QColor", shadowColor, setShadowColor)
    
    def fill(self):
        return self._fillColor
    
    @pyqtSignature("QColor")
    def setFill(self, value):
        self._fillColor = value
        self.emit(SIGNAL("contentsChanged()"))
        self.update()
    
    fill = pyqtProperty("QColor", fill, setFill)
    
    def lines(self):
        return self._lines
    
    @pyqtSignature("int")
    def setLines(self, value):
        self._lines = value
        self.emit(SIGNAL("contentsChanged()"))
        self.update()
    
    linesColor = pyqtProperty("QColor", lines, setLines)
    
    def linesColor(self):
        return self._linesColor
    
    @pyqtSignature("QColor")
    def setLinesColor(self, value):
        self._linesColor = value
        self.emit(SIGNAL("contentsChanged()"))
        self.update()
    
    linesColor = pyqtProperty("QColor", linesColor, setLinesColor)
    
    def enableEffect(self, effect, parameter, enable, override = True):
    
        if enable:
            self._enabledEffects[effect] = parameter
            if override and self._enabledEffects.has_key(self.paintOutline):
                del self._enabledEffects[self.paintOutline]
        else:
            if self._enabledEffects.has_key(effect):
                del self._enabledEffects[effect]
                if not self._enabledEffects:
                    self._enabledEffects[self.paintOutline] = Qt.DashLine
        
        self.emit(SIGNAL("contentsChanged()"))
        self.update()
    
    def paintFill(self, painter, path, color = Qt.red):
    
        painter.save()
        painter.setBrush(QBrush(self._fillColor))
        painter.setPen(Qt.NoPen)
        painter.drawPath(path)
        painter.restore()
    
    def fillEnabled(self):
        return self._enabledEffects.has_key(self.paintFill)
    
    @pyqtSignature("bool")
    def setFillEnabled(self, enable):
        self.enableEffect(self.paintFill, self._fillColor, enable)
    
    fillEnabled = pyqtProperty("bool", fillEnabled, setFillEnabled)
    
    def paintShadow(self, painter, path):
    
        spread = self._shadow
        if spread == 0:
            return
        
        alpha = 255/(spread**2)
        painter.save()
        color = QColor(self._shadowColor)
        color.setAlpha(alpha)
        painter.setBrush(color)
        painter.setPen(Qt.NoPen)
        painter.translate(-spread, -spread)
        
        for i in range(-spread, spread + 1):
            
            painter.save()
            for j in range(-spread, spread + 1):
            
                painter.drawPath(path)
                painter.translate(1, 0)
            
            painter.restore()
            painter.translate(0, 1)
        
        painter.restore()
    
    def shadowEnabled(self):
        return self._enabledEffects.has_key(self.paintShadow)
    
    @pyqtSignature("bool")
    def setShadowEnabled(self, enable):
        self.enableEffect(self.paintShadow, self._shadow, enable)
    
    shadowEnabled = pyqtProperty("bool", shadowEnabled, setShadowEnabled)
    
    def paintBackground(self, painter, path):
    
        pathRect = path.boundingRect()
        pathRect.adjust(-16, -16, 16, 16)
        
        painter.save()
        painter.fillRect(pathRect, QBrush(self._background))
        painter.restore()
    
    def backgroundEnabled(self):
        return self._enabledEffects.has_key(self.paintBackground)
    
    @pyqtSignature("bool")
    def setBackgroundEnabled(self, enable):
        self.enableEffect(self.paintBackground, self._background, enable, False)
    
    backgroundEnabled = pyqtProperty("bool", backgroundEnabled, setBackgroundEnabled)
    
    def paintOutline(self, painter, path):
    
        pen = QPen(Qt.DashLine)
        painter.save()
        painter.setPen(pen)
        painter.drawPath(path)
        painter.restore()
    
    def paintLines(self, painter, path):
    
        pen = QPen()
        pen.setBrush(QBrush(self._linesColor))
        
        pathRect = path.boundingRect()
        pathRect.adjust(-16, -16, 16, 16)
        left = int(pathRect.left())
        right = int(pathRect.right())
        top = int(pathRect.top())
        bottom = int(pathRect.bottom())
        
        painter.save()
        painter.setPen(pen)
        painter.setClipPath(path)
        random.seed(self._enabledEffects[self.paintLines])
        for i in range(self._lines):
            x1, x2 = random.randrange(left, right), random.randrange(left, right)
            y1, y2 = random.randrange(top, bottom), random.randrange(top, bottom)
            painter.drawLine(x1, y1, x2, y2)
        painter.restore()
    
    def linesEnabled(self):
        return self._enabledEffects.has_key(self.paintLines)
    
    @pyqtSignature("bool")
    def setLinesEnabled(self, enable):
        self.enableEffect(self.paintLines, random.random(), enable)
    
    linesEnabled = pyqtProperty("bool", linesEnabled, setLinesEnabled)
