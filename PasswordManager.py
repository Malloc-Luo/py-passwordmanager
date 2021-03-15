# -*- coding: utf-8 -*-
""" 主函数
在Main对象中调用别的窗口及连接不同窗口间的信号和槽
"""
import sys, os
sys.path.append(os.getcwd())
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QObject, QTimer, Qt
# from AddItemUi import AddItemUi
from Login import LoginUi, SigninUi
from MainGUI import MainGUI
from DataBase import DataBase
from Common import is_first_to_use
from Setting import Setting
from TipUi import TipUi


class Main(QObject):
    def __init__(self):
        super().__init__()
        self.isFirstUse = is_first_to_use()
        self.ui_loginW = LoginUi()
        self.ui_mainW = MainGUI()
        self.database = DataBase()
        self.timer = QTimer()
        self.ui_siginW = None
        self.init_connect()
        # 子窗口是否被打开
        self.isSubWOpened = False

    def init_connect(self):
        self.ui_loginW.loginSignal.connect(self.call_for_maingui)
        self.ui_loginW.sendSignal.connect(self.ui_mainW.get_admin_password)
        self.timer.timeout.connect(self.timeout_function)
        self.ui_mainW.openSubWSignal.connect(self.get_subW_state)
        # 与数据库连接
        self.ui_mainW.loadItemSignal.connect(self.database.load_items)
        self.ui_mainW.deleteItemSignal.connect(self.database.delete_useritem)
        self.ui_mainW.addItemSignal.connect(self.database.add_useritem)
        self.ui_mainW.modifySignal.connect(self.database.modify_useritem)
        self.ui_mainW.filiteSignal.connect(self.database.filite_useritem)
        self.database.sendUserItemsSignal.connect(self.ui_mainW.load_items)
        self.database.deleteItemSignal.connect(self.ui_mainW.get_delete_res)
        self.database.addItemSignal.connect(self.ui_mainW.get_add_res)
        self.database.filiteResSignal.connect(self.ui_mainW.get_filite_id)
        self.database.modifySignal.connect(self.ui_mainW.get_edit_res)
        # self.ui_loginW.sendDBNameSignal.connect(self.database.get_db_name)
        self.ui_loginW.sendDBRenameSignal.connect(self.database.get_new_name)
        self.ui_loginW.broadcastSettingSignal.connect(self.ui_mainW.get_setting)
        self.ui_loginW.broadcastSettingSignal.connect(self.database.get_setting)
        self.ui_mainW.ui_settingW.broadcastSettingSignal.connect(self.database.get_setting)
        self.ui_loginW.broadcastSettingSignal.connect(self.get_setting)
        self.ui_mainW.ui_settingW.broadcastSettingSignal.connect(self.get_setting)

    def start(self):
        # 如果是第一次用这个程序
        if self.isFirstUse is True:
            self.ui_siginW = SigninUi()
            self.ui_siginW.siginSignal.connect(self.call_for_loginui)
            self.ui_siginW.show()
        else:
            self.call_for_loginui()

    # 对内槽函数
    def call_for_maingui(self, status: bool):
        if status is True:
            self.ui_mainW.show()
            if self.isSubWOpened is True:
                self.ui_mainW.addItemUi.show()
            self.timer.start(self.timeForClose)
            self.ui_mainW.installEventFilter(self)
        else:
            self.tip = TipUi('密码错误', TipUi.ERROR)
            self.tip.show()

    def call_for_loginui(self):
        self.ui_loginW.show()

    def timeout_function(self):
        self.timer.stop()
        self.ui_mainW.hide()
        if self.isSubWOpened is True:
            self.ui_mainW.addItemUi.hide()
        self.start()

    def eventFilter(self, obj, event):
        if obj is self.ui_mainW or obj is self.ui_mainW.addItemUi or \
           obj is self.ui_mainW.ui_aboutW or obj is self.ui_mainW.ui_settingW:
            self.timer.start(self.timeForClose)
        return QObject.eventFilter(self, obj, event)

    def get_subW_state(self, state: bool):
        self.isSubWOpened = state
        if state is True:
            self.ui_mainW.addItemUi.installEventFilter(self)

    def get_setting(self, setting: Setting):
        self.setting = setting
        self.timeForClose = self.setting.autoLockTime * 60000


def main():
    if hasattr(Qt, 'AA_EnableHighDpiScaling'):
        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    if hasattr(Qt, 'AA_UseHighDpiPixmaps'):
        QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    app = QApplication(sys.argv)
    w = Main()
    w.start()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
