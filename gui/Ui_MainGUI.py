# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\FileBox\Code\Python\PasswordManager\py-passwordmanager\gui\MainGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(951, 815)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/mainui/icon/MainIcon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("QWidget {background:rgb(248, 248, 248);}\n"
"\n"
"QToolTip{\n"
"    border:0px solid rgb(118, 118, 118); \n"
"    background-color: #ffffff;\n"
"    color:#484848; \n"
"}\n"
"")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(1, 1, 1, 3)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("QTabWidget::pane {\n"
"    border-color: #cccccc;\n"
"}\n"
"QTabBar::tab {\n"
"    min-width:90px;\n"
"    color: #333333;\n"
"    border: 2px solid;\n"
"    padding:2px;\n"
"    border-radius:5px;\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.494737 rgba(220, 220, 220, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-color:rgb(220, 220, 220);\n"
"    margin-right:2px;\n"
"}\n"
"\n"
"QTabBar::tab:selected{\n"
"    /*min-width:120px;\n"
"    margin-left:50px;\n"
"    margin-right:50px;\n"
"    min-height:40px;*/\n"
"    color: #1296DB;\n"
"    border-top: 2px solid;\n"
"    border-color: white;\n"
"    border-top-color:#1296DB;\n"
"    background-color:white;\n"
"}\n"
"QTabBar::tab:hover {\n"
"    color:#1296DB;\n"
"}\n"
"\n"
"QCheckBox {\n"
"    padding: 2px;margin: 2px;\n"
"    background:Transparent;\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 15px;\n"
"    height: 15px;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    border-radius:4px;\n"
"    border-style:solid;\n"
"    border-width:2px;\n"
"    border-color:#34495E;\n"
"      background-color:rgb(255,255,255);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    border-radius:4px;\n"
"    border-style:solid;\n"
"    border-width:2px;\n"
"    border-color:#0078d7; \n"
"    image: url(:/mainui/icon/selected.png);\n"
"}\n"
"QCheckBox::indicator:hover{\n"
"    border-color:#0078d7; \n"
"}\n"
"QCheckBox:hover {\n"
"    color:rgb(0, 0, 216);\n"
"}\n"
"\n"
"/*\n"
" * SpinBox \n"
" */\n"
"QSpinBox {\n"
"    border-style:solid;\n"
"    border-width:2px;\n"
"    border-radius:6px;\n"
"    border-color:#34495E;\n"
"    padding-left:3px;\n"
"    padding-right:3px;\n"
"    margin: 1px;\n"
"}\n"
"QSpinBox:hover{\n"
"    color:rgb(0, 0, 216);\n"
"    border-color:#0078d7;\n"
"}\n"
"QSpinBox::up-button {\n"
"    padding:1px;\n"
"    background-color:transparent;\n"
"}\n"
"QSpinBox::down-button {\n"
"    padding:1px;\n"
"    background-color:transparent;\n"
"}\n"
"QSpinBox::down-button {\n"
"    padding:1px;\n"
"    background-color:transparent;\n"
"}\n"
"/* 向上箭头*/\n"
"QSpinBox::up-arrow {\n"
"    image:url(:/mainui/icon/up1.png);\n"
"    height: 15px;\n"
"}\n"
"QSpinBox::up-arrow:hover {\n"
"    \n"
"    image: url(:/mainui/icon/up0.png);\n"
"    height: 15px;\n"
"}\n"
"QSpinBox::up-arrow:pressed {\n"
"    \n"
"    image: url(:/mainui/icon/up0.png);\n"
"    height: 13px;\n"
"}\n"
"/*向下箭头*/\n"
"QSpinBox::down-arrow {\n"
"    image: url(:/mainui/icon/down1.png);\n"
"    height: 15px;\n"
"}\n"
"QSpinBox::down-arrow:hover {\n"
"    image: url(:/mainui/icon/down0.png);\n"
"    height: 15px;\n"
"}\n"
"QSpinBox::down-arrow:pressed {\n"
"    image: url(:/mainui/icon/down0.png);\n"
"    height: 13px;\n"
"}\n"
"/*\n"
" * groupbox\n"
" */\n"
"QGroupBox {\n"
"    background-color:#E5E5E5;\n"
"    border-color:#E5E5E5;\n"
"    border-radius:20px;\n"
"    padding:3px;\n"
"    margin:5px;\n"
"}\n"
"QGroupBox:hover {\n"
"    background-color:#e6e6e6;\n"
"    padding:5px;\n"
"}\n"
"QGroupBox::title {\n"
"    color: rgb(0, 0, 0);\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    left:10px;\n"
"    top:10px;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"QLabel {\n"
"    background:Transparent;\n"
"}\n"
"")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.South)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab0 = QtWidgets.QWidget()
        self.tab0.setObjectName("tab0")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab0)
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_2.setSpacing(4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.le_filiter = QtWidgets.QLineEdit(self.tab0)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_filiter.sizePolicy().hasHeightForWidth())
        self.le_filiter.setSizePolicy(sizePolicy)
        self.le_filiter.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.le_filiter.setFont(font)
        self.le_filiter.setStyleSheet("QLineEdit {\n"
"    border-style:none;\n"
"    padding:3px;\n"
"    border-radius:11px;\n"
"    border:2px solid #DCE4EC;\n"
"    background:rgb(255, 255, 255);\n"
"}\n"
"QLineEdit:focus {\n"
"    border:2px solid #34495E;\n"
"    background:rgb(255, 255, 255);\n"
"}\n"
"")
        self.le_filiter.setObjectName("le_filiter")
        self.horizontalLayout_2.addWidget(self.le_filiter)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.comboBox = QtWidgets.QComboBox(self.tab0)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.comboBox.setFont(font)
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox.setStyleSheet("\n"
"QComboBox {\n"
"    border: 1px solid gray;   /* 边框 */\n"
"    border-radius: 3px;   /* 圆角 */\n"
"    padding: 1px 18px 1px 3px;   /* 字体填衬 */\n"
"    color:#FFFFFF;\n"
"    background:#34495E;\n"
"}\n"
"/* 下拉后，整个下拉窗体样式 */\n"
"QComboBox QAbstractItemView {\n"
"    /* 选定项的虚框 */\n"
"    outline: 0px solid gray;\n"
"    /* 整个下拉窗体的边框 */   \n"
"    border: 1px solid white;   \n"
"    color:#FFFFFF;\n"
"    background:rgb(68, 96, 124);\n"
"}\n"
"\n"
"")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox)
        spacerItem1 = QtWidgets.QSpacerItem(380, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.pbt_about = QtWidgets.QPushButton(self.tab0)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbt_about.sizePolicy().hasHeightForWidth())
        self.pbt_about.setSizePolicy(sizePolicy)
        self.pbt_about.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pbt_about.setToolTipDuration(0)
        self.pbt_about.setStyleSheet("QPushButton\n"
"{\n"
"    padding:6px;\n"
"    border: 0px;\n"
"    background-color:transparent;\n"
"    image: url(:/mainui/icon/ab1.png);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    border: 0px;\n"
"    background-color:transparent;\n"
"    image: url(:/mainui/icon/ab0.png);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"    padding:6px;\n"
"}")
        self.pbt_about.setText("")
        self.pbt_about.setObjectName("pbt_about")
        self.horizontalLayout_2.addWidget(self.pbt_about)
        self.pbt_setting = QtWidgets.QPushButton(self.tab0)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbt_setting.sizePolicy().hasHeightForWidth())
        self.pbt_setting.setSizePolicy(sizePolicy)
        self.pbt_setting.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pbt_setting.setStyleSheet("QPushButton\n"
"{\n"
"    padding:6px;\n"
"    border: 0px;\n"
"    background-color:transparent;\n"
"    image: url(:/mainui/icon/set1.png);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    border: 0px;\n"
"    background-color:transparent;\n"
"    image: url(:/mainui/icon/set0.png);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"    padding:6px;\n"
"}")
        self.pbt_setting.setText("")
        self.pbt_setting.setObjectName("pbt_setting")
        self.horizontalLayout_2.addWidget(self.pbt_setting)
        self.pushButton = QtWidgets.QPushButton(self.tab0)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setAcceptDrops(True)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("QPushButton\n"
"{\n"
"    padding:6px;\n"
"    border: 0px;\n"
"    background-color:transparent;\n"
"    image: url(:/mainui/icon/delete1.png);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    border: 0px;\n"
"    background-color:transparent;\n"
"    image: url(:/mainui/icon/delete.png);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"    padding:6px;\n"
"}")
        self.pushButton.setText("")
        self.pushButton.setIconSize(QtCore.QSize(23, 23))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pbt_add = QtWidgets.QPushButton(self.tab0)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbt_add.sizePolicy().hasHeightForWidth())
        self.pbt_add.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.pbt_add.setFont(font)
        self.pbt_add.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pbt_add.setStyleSheet("QPushButton\n"
"{\n"
"    padding:6px;\n"
"    border: 0px;\n"
"    background-color:transparent;\n"
"    image: url(:/mainui/icon/add.png);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    border: 0px;\n"
"    background-color:transparent;\n"
"    image: url(:/mainui/icon/add1.png);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"    padding:6px;\n"
"}")
        self.pbt_add.setText("")
        self.pbt_add.setIconSize(QtCore.QSize(23, 23))
        self.pbt_add.setObjectName("pbt_add")
        self.horizontalLayout_2.addWidget(self.pbt_add)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.table = QtWidgets.QTableWidget(self.tab0)
        self.table.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.table.setStyleSheet("QTableWidget {\n"
"    color:#34495E;\n"
"    background:#DCDCDC;\n"
"    border:1px solid #b6b6b6;\n"
"    alternate-background-color:#d2d2d2;\n"
"    gridline-color:#ffffff;\n"
"    font-family:\'consolas,Microsoft YaHei\';\n"
"    font-size:10pt;\n"
"}\n"
"QTableWidget::item{\n"
"    border-radius:6px;\n"
"}\n"
"QTableWidget::item:selected{\n"
"color:#ffffff;\n"
"background:#73A1D0;\n"
"}\n"
"\n"
"QTableWidget::item:hover{\n"
"background:#5E84AA;\n"
"color:#000000;\n"
"    font-size:10;\n"
"}\n"
"QHeaderView::section{\n"
"text-align:center;\n"
"background:#496684;\n"
"padding:2px;\n"
"margin:1px;\n"
"color:#ffffff;\n"
"border:1px solid #242424;\n"
"border-left-width:0;\n"
"border-radius:4px;\n"
"}\n"
"QScrollBar:vertical{\n"
"background:#484848;\n"
"padding:0px;\n"
"border-radius:6px;\n"
"max-width:12px;\n"
"}\n"
"QScrollBar::handle:vertical{\n"
"background:#CCCCCC;\n"
"}\n"
"QScrollBar::handle:hover:vertical,QScrollBar::handle:pressed:vertical{\n"
"background:#A7A7A7;\n"
"}\n"
"QScrollBar::sub-page:vertical{\n"
"background:444444;\n"
"}\n"
"QScrollBar::add-page:vertical{\n"
"background:5B5B5B;\n"
"}\n"
"QScrollBar::add-line:vertical{\n"
"background:none;\n"
"}\n"
"QScrollBar::sub-line:vertical{\n"
"background:none;\n"
"}\n"
"")
        self.table.setLineWidth(1)
        self.table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)
        self.table.setDefaultDropAction(QtCore.Qt.CopyAction)
        self.table.setAlternatingRowColors(True)
        self.table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table.setTextElideMode(QtCore.Qt.ElideRight)
        self.table.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.table.setGridStyle(QtCore.Qt.SolidLine)
        self.table.setObjectName("table")
        self.table.setColumnCount(6)
        self.table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table.setHorizontalHeaderItem(5, item)
        self.table.horizontalHeader().setVisible(True)
        self.table.horizontalHeader().setCascadingSectionResizes(True)
        self.table.horizontalHeader().setDefaultSectionSize(140)
        self.table.horizontalHeader().setMinimumSectionSize(100)
        self.table.horizontalHeader().setSortIndicatorShown(True)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setVisible(False)
        self.table.verticalHeader().setDefaultSectionSize(40)
        self.table.verticalHeader().setHighlightSections(True)
        self.table.verticalHeader().setMinimumSectionSize(28)
        self.table.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.table)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/mainui/icon/mgr1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(":/mainui/icon/mgr0.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon1.addPixmap(QtGui.QPixmap(":/mainui/icon/mgr0.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab0, icon1, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "密码管理器"))
        self.le_filiter.setPlaceholderText(_translate("Form", "筛选"))
        self.comboBox.setItemText(0, _translate("Form", "全部"))
        self.comboBox.setItemText(1, _translate("Form", "名称"))
        self.comboBox.setItemText(2, _translate("Form", "账号"))
        self.comboBox.setItemText(3, _translate("Form", "邮箱/电话"))
        self.pbt_about.setToolTip(_translate("Form", "关于"))
        self.pbt_setting.setToolTip(_translate("Form", "设置"))
        self.pushButton.setToolTip(_translate("Form", "删除项"))
        self.pushButton.setShortcut(_translate("Form", "Del"))
        self.pbt_add.setToolTip(_translate("Form", "添加项"))
        self.pbt_add.setShortcut(_translate("Form", "Ctrl+N"))
        self.table.setSortingEnabled(True)
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("Form", "id"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("Form", "名称"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("Form", "账号"))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("Form", "密码"))
        item = self.table.horizontalHeaderItem(4)
        item.setText(_translate("Form", "邮箱/电话"))
        item = self.table.horizontalHeaderItem(5)
        item.setText(_translate("Form", "备注"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab0), _translate("Form", "密码管理"))
import gui.src.icons_rc
