# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget, QApplication, QGraphicsDropShadowEffect
from PyQt5.QtCore import pyqtSignal, Qt, QObject, QEvent
from PyQt5.QtGui import QColor
from gui.Ui_AddItem import Ui_Dialog
from UserItem import UserItem
from GenPasswordUi import GenPasswordUi
from MessageBox import MessageBox
from WidgetEffect import set_shadow_effect
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
        self.isChanged = False
        self.ui.le_name.installEventFilter(self)
        self.ui.le_account.installEventFilter(self)
        self.ui.le_password.installEventFilter(self)
        self.ui.le_email_or_phone.installEventFilter(self)
        self.ui.te_note.installEventFilter(self)
        set_shadow_effect(self.ui.pbt_add, radius=30)
        set_shadow_effect(self.ui.pbt_cancel, radius=30)

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
        if len(self.ui.le_name.text().strip()) == 0 or len(self.ui.le_account.text().strip()) == 0 or len(self.ui.le_password.text().strip()) == 0:
            self.ui.pbt_add.setDisabled(True)
            self.setWindowTitle(u'添加密码')
            self.isChanged = False
        else:
            self.ui.pbt_add.setDisabled(False)
            self.setWindowTitle(u'添加密码*')
            self.isChanged = True

    def get_item_content(self):
        # 获取填写的内容
        name = self.ui.le_name.text()
        account = self.ui.le_account.text()
        password = self.ui.le_password.text()
        email_or_phone = self.ui.le_email_or_phone.text()
        note = self.ui.te_note.toPlainText().replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')
        self.isChanged = False
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
        TipUi.show_tip('已复制密码')

    def subW_closed_notify(self):
        # 子窗口被关闭的时候接收到信号
        self.subWCreated = False

    def eventFilter(self, widget, event):
        if widget in {self.ui.le_name, self.ui.le_account, self.ui.le_password, self.ui.le_email_or_phone, self.ui.te_note}:
            if event.type() == QEvent.FocusIn:
                set_shadow_effect(widget, color=QColor(0, 120, 210), radius=20)
            elif event.type() == QEvent.FocusOut:
                set_shadow_effect(widget, visible=False)
        return QObject.eventFilter(self, widget, event)

    def closeEvent(self, event):
        if self.isChanged is True:
            pbt = MessageBox.warning(self, u'添加密码', u'新建密码尚未保存，是否保存？', MessageBox.YES | MessageBox.NO | MessageBox.CANCEL)
            if pbt == MessageBox.YES:
                self.get_item_content()
                event.accept()
            elif pbt == MessageBox.NO:
                event.accept()
            elif pbt == MessageBox.CANCEL:
                event.ignore()
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
