# -*- coding:utf-8 -*-

from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QSizePolicy
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QIcon
from gui.Ui_MessageBox import Ui_Dialog
# import gui.src.icons_rc
import sys


class MessageBox(QDialog):
    """ 自定义MessageBox，继承自QDialog\n
    其中有3个static method可用: information, warning, error，使用方法与QMessageBox基本一致。\n
    Args:\n
        parent: 父窗口
        title: MessageBox窗口标题 Window Title
        text: 消息文本
        btype: 按钮，有五种类型按钮：YES, NO, CANCLE, CLOSE, OK
        default: 默认按钮，默认值为YES
    """
    # 仅支持这几个按键
    YES = 0x01
    NO = 0x02
    CANCEL = 0x04
    CLOSE = 0x08
    OK = 0x10
    # 返回值
    retValue = 0

    def __init__(self, parent, title: str, text: str, btype=YES, default=YES):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)
        self.setAttribute(Qt.WA_QuitOnClose, True)
        self.setWindowTitle(title)
        self.btnList = {}
        self.ui.lb_text.setText(text)
        self.create_button(btype)
        self.set_default_btn(btype, default)

    def create_button(self, btype):
        # 如果按钮是yes
        if btype & MessageBox.YES == MessageBox.YES:
            self.yesbtn = QPushButton(self)
            self.set_button(self.yesbtn, u'Yes')
            self.btnList[MessageBox.YES] = self.yesbtn
            self.yesbtn.clicked.connect(self.btn_yes)
        # 如果按钮是no
        if btype & MessageBox.NO == MessageBox.NO:
            self.nobtn = QPushButton(self)
            self.set_button(self.nobtn, u'No')
            self.btnList[MessageBox.NO] = self.nobtn
            self.nobtn.clicked.connect(self.btn_no)
        # 如果按钮是cancel
        if btype & MessageBox.CANCEL == MessageBox.CANCEL:
            self.cancelbtn = QPushButton(self)
            self.set_button(self.cancelbtn, u'Cancel')
            self.btnList[MessageBox.CANCEL] = self.cancelbtn
            self.cancelbtn.clicked.connect(self.btn_cancel)
        # 如果按钮是close
        if btype & MessageBox.CLOSE == MessageBox.CLOSE:
            self.closebtn = QPushButton(self)
            self.set_button(self.closebtn, u'Close')
            self.btnList[MessageBox.CLOSE] = self.closebtn
            self.closebtn.clicked.connect(self.btn_close)
        # 如果按钮是ok
        if btype & MessageBox.OK == MessageBox.OK:
            self.okbtn = QPushButton(self)
            self.set_button(self.okbtn, u'Ok')
            self.btnList[MessageBox.OK] = self.okbtn
            self.okbtn.clicked.connect(self.btn_ok)

    def set_default_btn(self, btype, default):
        # default键必须是一个独立的按键
        if default not in {MessageBox.YES, MessageBox.NO, MessageBox.CANCEL, MessageBox.OK, MessageBox.CLOSE}:
            return
        if default & btype != 0:
            self.btnList[default].setDefault(True)

    def set_button(self, btn: QPushButton, text: str):
        # 设置按钮的一些参数
        btn.setText(text)
        btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        btn.setFixedSize(QSize(95, 38))
        self.ui.hlayout.addWidget(btn)

    def btn_yes(self):
        MessageBox.retValue = MessageBox.YES
        self.close()

    def btn_no(self):
        MessageBox.retValue = MessageBox.NO
        self.close()

    def btn_cancel(self):
        MessageBox.retValue = MessageBox.CANCEL
        self.close()

    def btn_close(self):
        MessageBox.retValue = MessageBox.CLOSE
        self.close()

    def btn_ok(self):
        MessageBox.retValue = MessageBox.OK
        self.close()

    def ret_val(self):
        return MessageBox.retValue

    # 使用时调用的静态方法
    @staticmethod
    def information(parent, title, text, btype=YES, default=YES):
        box = MessageBox(parent, title, text, btype, default)
        box.ui.pbt_icon.setIcon(QIcon(QPixmap(":/mainui/icon/notify.png")))
        box.exec()
        return box.ret_val()

    @staticmethod
    def warning(parent, title, text, btype=YES, default=YES):
        box = MessageBox(parent, title, text, btype, default)
        box.ui.pbt_icon.setIcon(QIcon(QPixmap(":/mainui/icon/warning.png")))
        box.exec()
        return box.ret_val()

    @staticmethod
    def error(parent, title, text, btype=YES, default=YES):
        box = MessageBox(parent, title, text, btype, default)
        box.ui.pbt_icon.setIcon(QIcon(QPixmap(":/mainui/icon/error.png")))
        box.exec()
        return box.ret_val()

    @staticmethod
    def question(parent, title, text, btype=YES, default=YES):
        box = MessageBox(parent, title, text, btype, default)
        box.ui.pbt_icon.setIcon(QIcon(QPixmap(":/mainui/icon/question.png")))
        box.exec()
        return box.ret_val()

    @staticmethod
    def success(parent, title, text, btype=YES, default=YES):
        box = MessageBox(parent, title, text, btype, default)
        box.ui.pbt_icon.setIcon(QIcon(QPixmap(":/mainui/icon/success.png")))
        box.exec()
        return box.ret_val()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MessageBox.error(None, 'messagebx', '这是一个messagebox', MessageBox.OK | MessageBox.CANCEL)
    MessageBox.information(None, 'messagebx', '这是一个messagebox', MessageBox.OK | MessageBox.CANCEL)
    MessageBox.success(None, 'messagebx', '这是一个messagebox', MessageBox.OK | MessageBox.CANCEL)
    MessageBox.question(None, 'messagebx', '这是一个messagebox', MessageBox.OK | MessageBox.CANCEL)
    MessageBox.warning(None, 'messagebx', '这是一个messagebox', MessageBox.OK | MessageBox.CANCEL)
    sys.exit(app.exec_())
