# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'clusterization_dialog.ui'
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

class Ui_ClusterizationDialog(object):
    def setupUi(self, ClusterizationDialog):
        ClusterizationDialog.setObjectName(_fromUtf8("ClusterizationDialog"))
        ClusterizationDialog.resize(400, 146)
        self.buttonBox = QtGui.QDialogButtonBox(ClusterizationDialog)
        self.buttonBox.setGeometry(QtCore.QRect(50, 110, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayoutWidget = QtGui.QWidget(ClusterizationDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 91))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.newmangirvan_radiobutton = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.newmangirvan_radiobutton.setObjectName(_fromUtf8("newmangirvan_radiobutton"))
        self.horizontalLayout.addWidget(self.newmangirvan_radiobutton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.other_radiobutton = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.other_radiobutton.setObjectName(_fromUtf8("other_radiobutton"))
        self.horizontalLayout_2.addWidget(self.other_radiobutton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(ClusterizationDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ClusterizationDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ClusterizationDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ClusterizationDialog)

    def retranslateUi(self, ClusterizationDialog):
        ClusterizationDialog.setWindowTitle(QtGui.QApplication.translate("ClusterizationDialog", "Clusterization", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ClusterizationDialog", "Choose Method:", None, QtGui.QApplication.UnicodeUTF8))
        self.newmangirvan_radiobutton.setText(QtGui.QApplication.translate("ClusterizationDialog", "Newman and Girvan", None, QtGui.QApplication.UnicodeUTF8))
        self.other_radiobutton.setText(QtGui.QApplication.translate("ClusterizationDialog", "Other", None, QtGui.QApplication.UnicodeUTF8))

