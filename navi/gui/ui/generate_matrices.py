# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'generate_matrices.ui'
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

class Ui_GenerateMatrices(object):
    def setupUi(self, GenerateMatrices):
        GenerateMatrices.setObjectName(_fromUtf8("GenerateMatrices"))
        GenerateMatrices.resize(400, 215)
        self.buttonBox = QtGui.QDialogButtonBox(GenerateMatrices)
        self.buttonBox.setGeometry(QtCore.QRect(50, 180, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayoutWidget = QtGui.QWidget(GenerateMatrices)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 161))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.threshold_input = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.threshold_input.setObjectName(_fromUtf8("threshold_input"))
        self.horizontalLayout.addWidget(self.threshold_input)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.adj_matrix_checkbox = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.adj_matrix_checkbox.setObjectName(_fromUtf8("adj_matrix_checkbox"))
        self.verticalLayout.addWidget(self.adj_matrix_checkbox)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.nbh_matrix_checkbox = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.nbh_matrix_checkbox.setObjectName(_fromUtf8("nbh_matrix_checkbox"))
        self.verticalLayout.addWidget(self.nbh_matrix_checkbox)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem1 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.rearrange_checkbox = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.rearrange_checkbox.setObjectName(_fromUtf8("rearrange_checkbox"))
        self.horizontalLayout_5.addWidget(self.rearrange_checkbox)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)

        self.retranslateUi(GenerateMatrices)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), GenerateMatrices.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), GenerateMatrices.reject)
        QtCore.QMetaObject.connectSlotsByName(GenerateMatrices)

    def retranslateUi(self, GenerateMatrices):
        GenerateMatrices.setWindowTitle(QtGui.QApplication.translate("GenerateMatrices", "Generate Matrices", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("GenerateMatrices", "Threshold or interval", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("GenerateMatrices", "Example: 50 or 30-50", None, QtGui.QApplication.UnicodeUTF8))
        self.adj_matrix_checkbox.setText(QtGui.QApplication.translate("GenerateMatrices", "Adjacency Matrix", None, QtGui.QApplication.UnicodeUTF8))
        self.nbh_matrix_checkbox.setText(QtGui.QApplication.translate("GenerateMatrices", "Neighbourhood Matrix", None, QtGui.QApplication.UnicodeUTF8))
        self.rearrange_checkbox.setText(QtGui.QApplication.translate("GenerateMatrices", "Rearrange", None, QtGui.QApplication.UnicodeUTF8))

