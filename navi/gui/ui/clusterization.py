# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'clusterization.ui'
#
# Created: Fri Oct 14 00:18:15 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Clusterize(object):
    def setupUi(self, Clusterize):
        Clusterize.setObjectName(_fromUtf8("Clusterize"))
        Clusterize.resize(681, 485)
        self.horizontalLayoutWidget = QtGui.QWidget(Clusterize)
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
        self.clusterize_button = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.clusterize_button.setObjectName(_fromUtf8("clusterize_button"))
        self.vboxlayout.addWidget(self.clusterize_button)
        self.network_graph_button = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.network_graph_button.setObjectName(_fromUtf8("network_graph_button"))
        self.vboxlayout.addWidget(self.network_graph_button)
        self.define_communities_button = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.define_communities_button.setObjectName(_fromUtf8("define_communities_button"))
        self.vboxlayout.addWidget(self.define_communities_button)
        self.export_data_button = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.export_data_button.setObjectName(_fromUtf8("export_data_button"))
        self.vboxlayout.addWidget(self.export_data_button)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.vboxlayout)

        self.retranslateUi(Clusterize)
        QtCore.QMetaObject.connectSlotsByName(Clusterize)

    def retranslateUi(self, Clusterize):
        Clusterize.setWindowTitle(QtGui.QApplication.translate("Clusterize", "Clusterization", None, QtGui.QApplication.UnicodeUTF8))
        self.clusterize_button.setText(QtGui.QApplication.translate("Clusterize", "Clusterize", None, QtGui.QApplication.UnicodeUTF8))
        self.network_graph_button.setText(QtGui.QApplication.translate("Clusterize", "Network Graph", None, QtGui.QApplication.UnicodeUTF8))
        self.define_communities_button.setText(QtGui.QApplication.translate("Clusterize", "Define Communities", None, QtGui.QApplication.UnicodeUTF8))
        self.export_data_button.setText(QtGui.QApplication.translate("Clusterize", "Export Data", None, QtGui.QApplication.UnicodeUTF8))

