# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\FileBox\Code\Python\PasswordManager\py-passwordmanager\gui\MessageBox.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 165)
        Dialog.setStyleSheet("QDialog {\n"
"    background-color:white;\n"
"}\n"
"QPushButton {\n"
"    border:2px solid rgb(0, 0, 127);\n"
"    padding:5px;\n"
"    border-radius:15px;\n"
"    color:#000000;\n"
"    background-color:transparent;\n"
"    font-family: \'Microsoft YaHei Ui\';\n"
"    font-size: 10pt;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"    color:#0078d7;\n"
"    background:rgb(255, 255, 255);\n"
"    border:2px solid #0078d7;\n"
"}\n"
"QPushButton:pressed {\n"
"    color:#000000;\n"
"    background:#B8C6D1;\n"
"}\n"
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pbt_icon = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbt_icon.sizePolicy().hasHeightForWidth())
        self.pbt_icon.setSizePolicy(sizePolicy)
        self.pbt_icon.setMinimumSize(QtCore.QSize(68, 64))
        self.pbt_icon.setStyleSheet("background-color: transparent;\n"
"border:none;")
        self.pbt_icon.setText("")
        self.pbt_icon.setIconSize(QtCore.QSize(64, 64))
        self.pbt_icon.setFlat(True)
        self.pbt_icon.setObjectName("pbt_icon")
        self.horizontalLayout.addWidget(self.pbt_icon)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.lb_text = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_text.sizePolicy().hasHeightForWidth())
        self.lb_text.setSizePolicy(sizePolicy)
        self.lb_text.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.lb_text.setFont(font)
        self.lb_text.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.lb_text.setWordWrap(True)
        self.lb_text.setObjectName("lb_text")
        self.horizontalLayout.addWidget(self.lb_text)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.hlayout = QtWidgets.QHBoxLayout()
        self.hlayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.hlayout.setObjectName("hlayout")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.hlayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.hlayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lb_text.setText(_translate("Dialog", "提示框"))
import gui.src.icons_rc
