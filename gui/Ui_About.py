# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\FileBox\Code\Python\PasswordManager\py-passwordmanager\gui\About.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(460, 380)
        Dialog.setMinimumSize(QtCore.QSize(460, 380))
        Dialog.setMaximumSize(QtCore.QSize(460, 380))
        Dialog.setFocusPolicy(QtCore.Qt.StrongFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/mainui/icon/secondmainicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setEnabled(False)
        self.pushButton_4.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/mainui/icon/MainIcon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(":/mainui/icon/MainIcon.ico"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(":/mainui/icon/MainIcon.ico"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_4.setFlat(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:#0078d7;")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 240))
        self.groupBox.setStyleSheet("border-color:red;\n"
"background-color:white;\n"
"border-radius:25px;\n"
"margin:5px;")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.verticalLayout.addWidget(self.groupBox)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.pbt_code = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pbt_code.setFont(font)
        self.pbt_code.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pbt_code.setStyleSheet("QPushButton {\n"
"    background:Transparent;\n"
"    border:2px solid Transparent;\n"
"    color:#34495E;\n"
"    padding:4px;\n"
"    padding-bottom:2px;\n"
"    qproperty-icon: url(:/mainui/icon/code1.png);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color:#0078d7;\n"
"    border-bottom-color:#0078d7;\n"
"    qproperty-icon: url(:/mainui/icon/code0.png);\n"
"}")
        self.pbt_code.setObjectName("pbt_code")
        self.horizontalLayout_2.addWidget(self.pbt_code)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.pbt_help = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pbt_help.setFont(font)
        self.pbt_help.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pbt_help.setStyleSheet("QPushButton {\n"
"    background:Transparent;\n"
"    border:2px solid Transparent;\n"
"    color:#34495E;\n"
"    padding:4px;\n"
"    padding-bottom:2px;\n"
"    qproperty-icon: url(:/mainui/icon/help1.png);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color:#0078d7;\n"
"    border-bottom-color:#0078d7;\n"
"    qproperty-icon: url(:/mainui/icon/help0.png);\n"
"}")
        self.pbt_help.setObjectName("pbt_help")
        self.horizontalLayout_2.addWidget(self.pbt_help)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.pbt_update = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pbt_update.setFont(font)
        self.pbt_update.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pbt_update.setStyleSheet("QPushButton {\n"
"    background:Transparent;\n"
"    border:2px solid Transparent;\n"
"    color:#34495E;\n"
"    padding:4px;\n"
"    padding-bottom:2px;\n"
"    qproperty-icon: url(:/mainui/icon/update1.png);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color:#0078d7;\n"
"    border-bottom-color:#0078d7;\n"
"    qproperty-icon: url(:/mainui/icon/update0.png);\n"
"}")
        self.pbt_update.setObjectName("pbt_update")
        self.horizontalLayout_2.addWidget(self.pbt_update)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem7 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem7)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "关于"))
        self.label.setText(_translate("Dialog", "version 0.9.7"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#000000;\">说明</span></p><p>本软件中的用户数据均储存在<span style=\" color:#000000;\">本地</span>，不会被上传到服务器.</p><p>一般情况下本软件不会主动连接到互联网，只有当用户主动使用检查更新功能时，才会连接网络，仅用于访问github网站提供的API，获取软件版本信息。</p><p>若在使用中遇到问题，可以点击<span style=\" text-decoration: underline; color:#0000ff;\">使用帮助</span>获取帮助。</p></body></html>"))
        self.pbt_code.setText(_translate("Dialog", "项目源码"))
        self.pbt_help.setText(_translate("Dialog", "使用帮助"))
        self.pbt_update.setText(_translate("Dialog", "检查更新"))
import gui.src.icons_rc