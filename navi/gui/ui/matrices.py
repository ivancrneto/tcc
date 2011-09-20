# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'matrices.ui'
#
# Created: Tue Sep 20 07:21:46 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Matrices(object):
    def setupUi(self, Matrices):
        Matrices.setObjectName(_fromUtf8("Matrices"))
        Matrices.resize(681, 485)
        self.horizontalLayoutWidget = QtGui.QWidget(Matrices)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 661, 471))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.matrix_tableview = QtGui.QTableView(self.horizontalLayoutWidget)
        self.matrix_tableview.setObjectName(_fromUtf8("matrix_tableview"))
        self.horizontalLayout.addWidget(self.matrix_tableview)
        self.vboxlayout = QtGui.QVBoxLayout()
        self.vboxlayout.setContentsMargins(0, -1, -1, -1)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.pushButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.vboxlayout.addWidget(self.pushButton)
        self.pushButton_4 = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.vboxlayout.addWidget(self.pushButton_4)
        self.pushButton_3 = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.vboxlayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.vboxlayout.addWidget(self.pushButton_2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem)
        self.pushButton_5 = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.vboxlayout.addWidget(self.pushButton_5)
        self.horizontalLayout.addLayout(self.vboxlayout)

        self.retranslateUi(Matrices)
        QtCore.QMetaObject.connectSlotsByName(Matrices)

    def retranslateUi(self, Matrices):
        Matrices.setWindowTitle(QtGui.QApplication.translate("Matrices", "Matrices and Threshold Analysis", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Matrices", "Generate Matrices", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("Matrices", "Network Graph", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("Matrices", "Color Matrix Graph", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Matrices", "Export Matrices", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.setText(QtGui.QApplication.translate("Matrices", "Analyse Thresholds", None, QtGui.QApplication.UnicodeUTF8))

