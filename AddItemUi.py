# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from gui.Ui_AddItem import Ui_Dialog
from UserItem import UserItem
import time
import sys


class AddItemUi(QWidget):
    # 发送一个UserItem对象
    userItemSignal = pyqtSignal(UserItem)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.isAddClicked = False
        self.set_connect_slot()
        # 隐藏警告标签
        self.ui.lb_name_warning.hide()
        self.ui.lb_account_warning.hide()
        self.ui.lb_pswd_warning.hide()

    def set_connect_slot(self):
        self.ui.pbt_cancel.clicked.connect(self.close)
        self.ui.pbt_add.clicked.connect(self.get_item_content)
        self.ui.le_name.cursorPositionChanged.connect(self.name_warning)
        self.ui.le_account.cursorPositionChanged.connect(self.account_warning)
        self.ui.le_password.cursorPositionChanged.connect(self.password_warning)

    def name_warning(self):
        if self.isAddClicked == True:
            if len(self.ui.le_name.text().replace(' ', '')) == 0:
                self.ui.lb_name_warning.show()
            else:
                self.ui.lb_name_warning.hide()

    def account_warning(self):
        if self.isAddClicked == True:
            if len(self.ui.le_account.text().replace(' ', '')) == 0:
                self.ui.lb_account_warning.show()
            else:
                self.ui.lb_account_warning.hide()

    def password_warning(self):
        if self.isAddClicked == True:
            if len(self.ui.le_password.text().replace(' ', '')) == 0:
                self.ui.lb_pswd_warning.show()
            else:
                self.ui.lb_pswd_warning.hide()

    def get_item_content(self):
        self.isAddClicked = True
        # 获取填写的内容
        name     = self.ui.le_name.text()
        account  = self.ui.le_account.text()
        password = self.ui.le_password.text()
        email_or_phone = self.ui.le_email_or_phone.text()
        note = self.ui.te_note.toPlainText()
        self.name_warning()
        self.account_warning()
        self.password_warning()
        # 发送UserItem对象
        if len(name.replace(' ', '')) != 0 and len(account.replace(' ', '')) != 0 and len(password.replace(' ', '')) != 0:
            ID = str(int(time.time() * 100))[-10:]
            self.emit_signal(UserItem(ID, name, account, email_or_phone, note).load_plaintext(password))
            self.close()

    def emit_signal(self, item):
        print(item)
        self.userItemSignal.emit(item)

    def closeEvent(self, event):
        """ 窗口关闭事件
        """
        self.isAddClicked = False
        self.ui.le_account.clear()
        self.ui.le_email_or_phone.clear()
        self.ui.le_name.clear()
        self.ui.le_password.clear()
        self.ui.te_note.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = AddItemUi()
    w.show()
    sys.exit(app.exec_())
