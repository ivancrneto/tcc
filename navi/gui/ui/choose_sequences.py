# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'choose_sequences.ui'
#
# Created: Sat Sep 24 14:26:53 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ChooseSequences(object):
    def setupUi(self, ChooseSequences):
        ChooseSequences.setObjectName(_fromUtf8("ChooseSequences"))
        ChooseSequences.resize(1030, 524)
        self.choice_buttons = QtGui.QDialogButtonBox(ChooseSequences)
        self.choice_buttons.setGeometry(QtCore.QRect(940, 10, 81, 241))
        self.choice_buttons.setOrientation(QtCore.Qt.Vertical)
        self.choice_buttons.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.choice_buttons.setObjectName(_fromUtf8("choice_buttons"))
        self.verticalLayoutWidget = QtGui.QWidget(ChooseSequences)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 921, 511))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.sequence_table = QtGui.QTableView(self.verticalLayoutWidget)
        self.sequence_table.setObjectName(_fromUtf8("sequence_table"))
        self.verticalLayout.addWidget(self.sequence_table)

        self.retranslateUi(ChooseSequences)
        QtCore.QObject.connect(self.choice_buttons, QtCore.SIGNAL(_fromUtf8("accepted()")), ChooseSequences.accept)
        QtCore.QObject.connect(self.choice_buttons, QtCore.SIGNAL(_fromUtf8("rejected()")), ChooseSequences.reject)
        QtCore.QMetaObject.connectSlotsByName(ChooseSequences)

    def retranslateUi(self, ChooseSequences):
        ChooseSequences.setWindowTitle(QtGui.QApplication.translate("ChooseSequences", "Choose Sequences", None, QtGui.QApplication.UnicodeUTF8))

