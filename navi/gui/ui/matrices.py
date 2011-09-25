# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'matrices.ui'
#
# Created: Sun Sep 25 18:06:34 2011
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
        self.generate_matrices_button = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.generate_matrices_button.setObjectName(_fromUtf8("generate_matrices_button"))
        self.vboxlayout.addWidget(self.generate_matrices_button)
        self.network_graph_button = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.network_graph_button.setObjectName(_fromUtf8("network_graph_button"))
        self.vboxlayout.addWidget(self.network_graph_button)
        self.color_matrix_graph_button = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.color_matrix_graph_button.setObjectName(_fromUtf8("color_matrix_graph_button"))
        self.vboxlayout.addWidget(self.color_matrix_graph_button)
        self.export_matrices_button = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.export_matrices_button.setObjectName(_fromUtf8("export_matrices_button"))
        self.vboxlayout.addWidget(self.export_matrices_button)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem)
        self.analyse_thresholds_button = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.analyse_thresholds_button.setObjectName(_fromUtf8("analyse_thresholds_button"))
        self.vboxlayout.addWidget(self.analyse_thresholds_button)
        self.horizontalLayout.addLayout(self.vboxlayout)

        self.retranslateUi(Matrices)
        QtCore.QMetaObject.connectSlotsByName(Matrices)

    def retranslateUi(self, Matrices):
        Matrices.setWindowTitle(QtGui.QApplication.translate("Matrices", "Matrices and Threshold Analysis", None, QtGui.QApplication.UnicodeUTF8))
        self.generate_matrices_button.setText(QtGui.QApplication.translate("Matrices", "Generate Matrices", None, QtGui.QApplication.UnicodeUTF8))
        self.network_graph_button.setText(QtGui.QApplication.translate("Matrices", "Network Graph", None, QtGui.QApplication.UnicodeUTF8))
        self.color_matrix_graph_button.setText(QtGui.QApplication.translate("Matrices", "Color Matrix Graph", None, QtGui.QApplication.UnicodeUTF8))
        self.export_matrices_button.setText(QtGui.QApplication.translate("Matrices", "Export Matrices", None, QtGui.QApplication.UnicodeUTF8))
        self.analyse_thresholds_button.setText(QtGui.QApplication.translate("Matrices", "Analyse Thresholds", None, QtGui.QApplication.UnicodeUTF8))

