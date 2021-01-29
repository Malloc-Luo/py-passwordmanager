# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt
from gui.Ui_AddItem import Ui_Dialog
from UserItem import UserItem
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
        self.set_connect_slot()
        self.setAttribute(Qt.WA_DeleteOnClose, True)

    def set_connect_slot(self):
        self.ui.pbt_cancel.clicked.connect(self.close)
        self.ui.pbt_add.clicked.connect(self.get_item_content)
        self.ui.le_name.cursorPositionChanged.connect(self.check_content)
        self.ui.le_account.cursorPositionChanged.connect(self.check_content)
        self.ui.le_password.cursorPositionChanged.connect(self.check_content)

    def check_content(self):
        if self.ui.le_name.text() == '' or self.ui.le_account.text() == '' or self.ui.le_password.text() == '':
            self.ui.pbt_add.setDisabled(True)
        else:
            self.ui.pbt_add.setDisabled(False)

    def get_item_content(self):
        # 获取填写的内容
        name     = self.ui.le_name.text()
        account  = self.ui.le_account.text()
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

    def closeEvent(self, event):
        """ 窗口关闭事件
        """
        self.closeSubWSignal.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = AddItemUi()
    w.show()
    sys.exit(app.exec_())
