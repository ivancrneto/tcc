# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'analyse_threshold_dialog.ui'
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

class Ui_AnalyseThresholdDialog(object):
    def setupUi(self, AnalyseThresholdDialog):
        AnalyseThresholdDialog.setObjectName(_fromUtf8("AnalyseThresholdDialog"))
        AnalyseThresholdDialog.resize(400, 127)
        self.buttonBox = QtGui.QDialogButtonBox(AnalyseThresholdDialog)
        self.buttonBox.setGeometry(QtCore.QRect(50, 90, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayoutWidget = QtGui.QWidget(AnalyseThresholdDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 79))
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
        self.distance_radiobutton = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.distance_radiobutton.setObjectName(_fromUtf8("distance_radiobutton"))
        self.horizontalLayout.addWidget(self.distance_radiobutton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.largestcluster_radiobutton = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.largestcluster_radiobutton.setObjectName(_fromUtf8("largestcluster_radiobutton"))
        self.horizontalLayout_2.addWidget(self.largestcluster_radiobutton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(AnalyseThresholdDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), AnalyseThresholdDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AnalyseThresholdDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AnalyseThresholdDialog)

    def retranslateUi(self, AnalyseThresholdDialog):
        AnalyseThresholdDialog.setWindowTitle(QtGui.QApplication.translate("AnalyseThresholdDialog", "Analyse Threshold", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AnalyseThresholdDialog", "Choose Method:", None, QtGui.QApplication.UnicodeUTF8))
        self.distance_radiobutton.setText(QtGui.QApplication.translate("AnalyseThresholdDialog", "Distance", None, QtGui.QApplication.UnicodeUTF8))
        self.largestcluster_radiobutton.setText(QtGui.QApplication.translate("AnalyseThresholdDialog", "Largest Cluster", None, QtGui.QApplication.UnicodeUTF8))

