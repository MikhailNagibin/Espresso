# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UI(object):
    def setupUi(self, UI):
        UI.setObjectName("UI")
        UI.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(UI)
        self.centralwidget.setObjectName("centralwidget")
        self.add = QtWidgets.QTableWidget(self.centralwidget)
        self.add.setGeometry(QtCore.QRect(133, 75, 533, 400))
        self.add.setObjectName("add")
        self.add.setColumnCount(0)
        self.add.setRowCount(0)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(660, 520, 121, 28))
        self.pushButton.setObjectName("pushButton")
        UI.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(UI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        UI.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(UI)
        self.statusbar.setObjectName("statusbar")
        UI.setStatusBar(self.statusbar)

        self.retranslateUi(UI)
        QtCore.QMetaObject.connectSlotsByName(UI)

    def retranslateUi(self, UI):
        _translate = QtCore.QCoreApplication.translate
        UI.setWindowTitle(_translate("UI", "MainWindow"))
        self.pushButton.setText(_translate("UI", "добавить кофе"))
