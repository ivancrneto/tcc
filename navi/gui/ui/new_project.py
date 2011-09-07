# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_project.ui'
#
# Created: Wed Sep  7 15:55:41 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_NewProject(object):
    def setupUi(self, NewProject):
        NewProject.setObjectName(_fromUtf8("NewProject"))
        NewProject.resize(395, 176)
        self.buttonBox = QtGui.QDialogButtonBox(NewProject)
        self.buttonBox.setGeometry(QtCore.QRect(40, 140, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayoutWidget = QtGui.QWidget(NewProject)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 371, 122))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.project_name_label = QtGui.QLabel(self.verticalLayoutWidget)
        self.project_name_label.setObjectName(_fromUtf8("project_name_label"))
        self.horizontalLayout.addWidget(self.project_name_label)
        self.project_name = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.project_name.setObjectName(_fromUtf8("project_name"))
        self.horizontalLayout.addWidget(self.project_name)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.project_path_label = QtGui.QLabel(self.verticalLayoutWidget)
        self.project_path_label.setObjectName(_fromUtf8("project_path_label"))
        self.horizontalLayout_2.addWidget(self.project_path_label)
        self.project_path = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.project_path.setObjectName(_fromUtf8("project_path"))
        self.horizontalLayout_2.addWidget(self.project_path)
        self.browse_project_button = QtGui.QPushButton(self.verticalLayoutWidget)
        self.browse_project_button.setObjectName(_fromUtf8("browse_project_button"))
        self.horizontalLayout_2.addWidget(self.browse_project_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_4.addWidget(self.label)
        self.database_path = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.database_path.setObjectName(_fromUtf8("database_path"))
        self.horizontalLayout_4.addWidget(self.database_path)
        self.browse_database_button = QtGui.QPushButton(self.verticalLayoutWidget)
        self.browse_database_button.setObjectName(_fromUtf8("browse_database_button"))
        self.horizontalLayout_4.addWidget(self.browse_database_button)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(NewProject)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), NewProject.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), NewProject.reject)
        QtCore.QMetaObject.connectSlotsByName(NewProject)

    def retranslateUi(self, NewProject):
        NewProject.setWindowTitle(QtGui.QApplication.translate("NewProject", "New Project", None, QtGui.QApplication.UnicodeUTF8))
        self.project_name_label.setText(QtGui.QApplication.translate("NewProject", "Project Name", None, QtGui.QApplication.UnicodeUTF8))
        self.project_path_label.setText(QtGui.QApplication.translate("NewProject", "Project Path", None, QtGui.QApplication.UnicodeUTF8))
        self.browse_project_button.setText(QtGui.QApplication.translate("NewProject", "Browse...", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("NewProject", "Database Path", None, QtGui.QApplication.UnicodeUTF8))
        self.browse_database_button.setText(QtGui.QApplication.translate("NewProject", "Browse...", None, QtGui.QApplication.UnicodeUTF8))

