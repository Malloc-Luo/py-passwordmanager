# -*- coding: utf-8 -*-

# 管理员数据库，用于验证密码
# 数据库名为 admin.db，数据表 admintable
# 数据表内容：
# +-----+------+
# | key | -----|
from Common import dbAbsPath, adminDataDb, get_admin_key, operatorSystem
from gui.Ui_LoginUi import Ui_Login
from gui.Ui_SigninUi import Ui_Signin
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal, Qt, QObject, QEvent
from PyQt5.QtGui import QFont
from MessageBox import MessageBox
from Setting import Setting
from WidgetEffect import set_shadow_effect
import sqlite3 as sql
import secrets
import string
import hashlib
import sys


def get_stamp(length: int) -> str:
    return ''.join([secrets.choice(string.hexdigits) for i in range(length)])


def get_md5hex(text: str) -> str:
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return str(md5.hexdigest())


class LoginUi(QWidget):
    # 登录信号，成功为true
    loginSignal = pyqtSignal(bool)
    # 发送管理员密码明文
    sendSignal = pyqtSignal(str)
    # 发送数据库名
    sendDBNameSignal = pyqtSignal(str)
    # 发送数据库重命名
    sendDBRenameSignal = pyqtSignal(str)
    # 加载设置并广播
    broadcastSettingSignal = pyqtSignal(Setting)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.ui.pbt_warning.hide()
        self.init_connect()
        self.ui.pushButton.setDisabled(True)
        self.ui.pushButton.setVisible(False)
        # 设置阴影
        set_shadow_effect(self.ui.widget, radius=35)
        set_shadow_effect(self.ui.lineEdit)
        set_shadow_effect(self.ui.pushButton, radius=30)
        # 如果是Linux系统，字体放大一点
        if operatorSystem == 'Linux':
            font = QFont()
            font.setFamily('Microsoft YaHei UI')
            font.setPointSize(11)
            self.ui.lineEdit.setFont(font)

    def init_connect(self):
        self.ui.pushButton.clicked.connect(self.submit_admin_password)
        self.ui.lineEdit.cursorPositionChanged.connect(self.pushbutton_style)

    def update_key(self):
        DBconnect = sql.connect(adminDataDb)
        DBcursor = DBconnect.cursor()
        stamp = get_stamp(15).lower()
        key = get_md5hex(self.adminpswd + stamp) + stamp
        DBcursor.execute('update admintable set key = ?', (key, ))
        DBcursor.close()
        DBconnect.commit()
        DBconnect.close()
        # 发送给数据库用于重命名，在数据库对象析构函数里面修改数据库名
        self.sendDBRenameSignal.emit(dbAbsPath + stamp + '.db')

    def closeEvent(self, event):
        self.ui.lineEdit.clear()

    # 对内槽函数
    def submit_admin_password(self):
        self.adminpswd = str(self.ui.lineEdit.text())
        key = get_admin_key()[0]
        # 如果数据库突然丢了或者没有读到数据则退出程序
        if key is None:
            MessageBox.error(self, '进入密码管理器', '发生错误，退出程序，请尝试重新启动', MessageBox.Yes)
            sys.exit()
        # 如果登录成功则需要更新储存的密码
        if get_md5hex(self.adminpswd + key[-15:]) == key[:-15]:
            self.ui.pbt_warning.hide()
            self.update_key()
            # 下面几个信号发送的顺序不能变！！！有特殊安排的
            # 向主界面发送管理员密码明文
            self.sendSignal.emit(self.adminpswd)
            # 发送数据库的名字，用这个打开数据库
            self.sendDBNameSignal.emit(dbAbsPath + key[-15:] + '.db')
            # 加载之后向外广播设置
            self.broadcastSettingSignal.emit(Setting(dbAbsPath + '.settings'))
            # 验证成功可以登录，发送信号打开主界面
            self.loginSignal.emit(True)
            self.close()
        else:
            self.ui.pbt_warning.show()
            self.loginSignal.emit(False)

    def pushbutton_style(self):
        if len(self.ui.lineEdit.text()) < 6:
            self.ui.pbt_warning.setVisible(False)
            self.ui.pushButton.setDisabled(True)
            self.ui.pushButton.setVisible(False)
            self.ui.widget.setGeometry(0, 0, 400, 230)
            self.ui.lineEdit.setGeometry(80, 110, 240, 48)
        else:
            self.ui.pushButton.setDisabled(False)
            self.ui.pushButton.setVisible(True)
            self.ui.widget.setGeometry(0, 0, 400, 150)
            self.ui.lineEdit.setGeometry(80, 60, 240, 48)


class SigninUi(QWidget):
    # 注册成功信号
    siginSignal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Signin()
        self.ui.setupUi(self)
        self.passby = False
        self.ui.pbt_setting.setDisabled(True)
        self.setAttribute(Qt.WA_DeleteOnClose, True)
        self.init_connect()
        set_shadow_effect(self.ui.pbt_cancel, radius=30)
        set_shadow_effect(self.ui.pbt_setting, radius=30)

    def init_connect(self):
        self.ui.pbt_cancel.clicked.connect(self.close)
        self.ui.pbt_setting.clicked.connect(self.create_admin_account)
        self.ui.le_pswd.cursorPositionChanged.connect(self.compare_password)
        self.ui.le_proof.cursorPositionChanged.connect(self.compare_password)

    # 对内槽函数
    def create_admin_account(self):
        DBconnect = sql.connect(adminDataDb)
        DBcursor = DBconnect.cursor()
        # 获取一个15位的戳
        stamp = get_stamp(15).lower()
        adminpwsd = str(self.ui.le_pswd.text())
        key = get_md5hex(adminpwsd + stamp) + stamp
        # 创建仓库
        DBcursor.execute('create table admintable (key varchar(150));')
        DBcursor.execute('insert into admintable values (?);', (key,))
        DBcursor.close()
        DBconnect.commit()
        DBconnect.close()
        MessageBox.information(self, '设置管理员密码', '设置成功！请妥善保管此密码\n如若丢失则无法找回', MessageBox.YES)
        self.siginSignal.emit()
        self.close()

    def compare_password(self):
        pswd, proof = self.ui.le_pswd.text(), self.ui.le_proof.text()
        if len(pswd) != 0 and len(proof) != 0:
            if proof != pswd:
                self.passby = False
                self.ui.warning.setText('密码不一致')
            elif len(pswd) < 6:
                self.passby = False
                self.ui.warning.setText('密码长度不能小于6！')
            else:
                self.passby = True
                self.ui.warning.setText('')
        else:
            ...
        self.ui.pbt_setting.setDisabled(not self.passby)
