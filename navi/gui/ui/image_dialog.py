# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'image_dialog.ui'
#
# Created: Mon Oct 17 21:32:14 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ImageDialog(object):
    def setupUi(self, ImageDialog):
        ImageDialog.setObjectName(_fromUtf8("ImageDialog"))
        ImageDialog.resize(674, 565)
        self.plot_frame = QtGui.QWidget(ImageDialog)
        self.plot_frame.setGeometry(QtCore.QRect(10, 19, 651, 501))
        self.plot_frame.setObjectName(_fromUtf8("plot_frame"))
        self.verticalLayoutWidget = QtGui.QWidget(ImageDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 520, 651, 41))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.navbar_layout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.navbar_layout.setMargin(0)
        self.navbar_layout.setObjectName(_fromUtf8("navbar_layout"))

        self.retranslateUi(ImageDialog)
        QtCore.QMetaObject.connectSlotsByName(ImageDialog)

    def retranslateUi(self, ImageDialog):
        ImageDialog.setWindowTitle(QtGui.QApplication.translate("ImageDialog", "Image Dialog", None, QtGui.QApplication.UnicodeUTF8))

