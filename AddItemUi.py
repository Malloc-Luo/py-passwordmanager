# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import pyqtSignal
from gui.Ui_AddItem import Ui_Dialog
from UserItem import UserItem
from GenPasswordUi import GenPasswordUi
from TipUi import TipUi
import time
import sys


class AddItemUi(QWidget):
    # 发送一个UserItem对象
    userItemSignal = pyqtSignal(UserItem)
    # 子窗口是否被打开
    closeSubWSignal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pbt_add.setDisabled(True)
        self.ui.pbt_gen.setFlat(True)
        self.ui_genW = GenPasswordUi()
        self.set_connect_slot()
        # self.setAttribute(Qt.WA_DeleteOnClose, True)
        self.subWCreated = False

    def set_connect_slot(self):
        self.ui.pbt_cancel.clicked.connect(self.close)
        self.ui.pbt_add.clicked.connect(self.get_item_content)
        self.ui.le_name.cursorPositionChanged.connect(self.check_content)
        self.ui.le_account.cursorPositionChanged.connect(self.check_content)
        self.ui.le_password.cursorPositionChanged.connect(self.check_content)
        self.ui.pbt_gen.clicked.connect(self.gen_password)
        # 连接密码添加界面的槽函数
        self.ui_genW.sendSignel.connect(self.add_password)
        self.ui_genW.tellSupWClosed.connect(self.subW_closed_notify)

    def check_content(self):
        if self.ui.le_name.text() == '' or self.ui.le_account.text() == '' or self.ui.le_password.text() == '':
            self.ui.pbt_add.setDisabled(True)
        else:
            self.ui.pbt_add.setDisabled(False)

    def get_item_content(self):
        # 获取填写的内容
        name = self.ui.le_name.text()
        account = self.ui.le_account.text()
        password = self.ui.le_password.text()
        email_or_phone = self.ui.le_email_or_phone.text()
        note = self.ui.te_note.toPlainText().replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')
        # 发送UserItem对象
        if len(name.replace(' ', '')) != 0 and len(account.replace(' ', '')) != 0 and len(password.replace(' ', '')) != 0:
            ID = str(int(time.time() * 100))[-10:]
            self.emit_signal(UserItem(ID, name, account, email_or_phone=email_or_phone, note=note, _plainpswd=password))
            self.close()

    def emit_signal(self, item):
        self.userItemSignal.emit(item)

    def gen_password(self):
        # self.ui_genW = GenPasswordUi()
        self.subWCreated = True
        self.ui_genW.show()

    def add_password(self, pswd):
        self.ui.le_password.setText(pswd)
        self.tip = TipUi('已复制密码')
        self.tip.show()

    def subW_closed_notify(self):
        # 子窗口被关闭的时候接收到信号
        self.subWCreated = False

    def closeEvent(self, event):
        # 关闭窗口事件，发送关闭信号
        self.closeSubWSignal.emit()

    def hideEvent(self, event):
        if self.subWCreated is True:
            self.ui_genW.hide()

    def showEvent(self, event):
        # 显示事件，如果子窗口被打开了则显示子窗口
        if self.subWCreated is True:
            self.ui_genW.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = AddItemUi()
    w.show()
    sys.exit(app.exec_())
