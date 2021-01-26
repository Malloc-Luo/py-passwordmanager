# -*- coding: utf-8 -*-

"""
    登录
    初次登录的时候要求设置密码，之后可以使用
"""
from Common import dbAbsPath, adminDataDb
from gui.Ui_LoginUi import Ui_Login
from gui.Ui_SigninUi import Ui_Signin
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox
from PyQt5.QtCore import QEvent, QObject, QSize, pyqtSignal, QRegExp
from PyQt5.QtGui import QHoverEvent, QMouseEvent
import sqlite3 as sql
import time
import sys

print(dbAbsPath)


class LoginUi(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.ui.pbt_warning.hide()
        self.ui.pushButton.installEventFilter(self)

    # 事件过滤器，处理鼠标动作特效
    def eventFilter(self, obj, event):
        if obj == self.ui.pushButton:
            if event.type() == QHoverEvent.Enter:
                self.ui.pushButton.setIconSize(QSize(80, 80))
            elif event.type() == QHoverEvent.Leave:
                self.ui.pushButton.setIconSize(QSize(70, 70))
            elif event.type() == QEvent.MouseButtonPress:
                self.ui.pushButton.setIconSize(QSize(70, 70))
            elif event.type() == QEvent.MouseButtonRelease:
                self.ui.pushButton.setIconSize(QSize(80, 80))
        return QObject.eventFilter(self, obj, event)

    def keyPressEvent(self, event):
        print('key press')

    # 对内槽函数
    def submit_admin_password(self):
        password = self.ui.lineEdit.text()


class SigninUi(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Signin()
        self.ui.setupUi(self)
        self.passby = False
        self.ui.warning.hide()
        self.ui.pbt_setting.setDisabled(True)
        self.init_connect()

    def init_connect(self):
        self.ui.pbt_cancel.clicked.connect(self.close)
        self.ui.pbt_setting.clicked.connect(self.create_admin_account)
        self.ui.le_pswd.cursorPositionChanged.connect(self.compare_password)
        self.ui.le_proof.cursorPositionChanged.connect(self.compare_password)
    # 对内槽函数
    def create_admin_account(self):
        DBconnect = sql.connect(adminDataDb)
        DBcursor = DBconnect.cursor()
        # 时间戳
        timestamp = str(int(time.time() * 100))
        adminpwsd = self.ui.le_pswd.text()
        key = hash(adminpwsd + timestamp)
        # 创建仓库
        DBcursor.execute('create table admintable (key varchar(100), timestamp varchar(20))')
        DBcursor.execute('insert into admintable (key, timestamp) values (?, ?)', (key, timestamp))
        DBcursor.close()
        DBconnect.commit()
        DBconnect.close()
        QMessageBox.information(self, '设置管理员密码', '设置成功！请妥善管理，无法找回', QMessageBox.Yes)
        self.close()

    def compare_password(self):
        pswd, proof = self.ui.le_pswd.text(), self.ui.le_proof.text()
        if len(pswd) != 0 and len(proof) != 0:
            if proof != pswd:
                self.passby = False
                self.ui.warning.show()
            else:
                self.passby = True
                self.ui.warning.hide()
        else:
            self.ui.warning.hide()
        self.ui.pbt_setting.setDisabled(not self.passby)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = SigninUi()
    w.show()
    sys.exit(app.exec_())