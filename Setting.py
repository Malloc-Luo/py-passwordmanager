# -*- coding:utf-8 -*-
import pickle as pkl
from Common import dbAbsPath
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal, Qt
from MessageBox import MessageBox
from TipUi import TipUi
from gui.Ui_SettingUi import Ui_settingDialog
import os


class Setting:
    """ 设置内容，目前支持的设置项：
        1. 无动作后自动锁定时间
        2. 显示tooltips
        3. 显示行号
        4. 删除时确认提示
        5. 使用正则表达式搜索
        6. 自动备份
        7. 按住Ctrl键显示密码
        8. 鼠标单击选中单元格
    """
    def __init__(self, path=None):
        try:
            # 配置文件位置，是一个序列化文件
            if path is not None and os.path.exists(path):
                with open(path, 'rb') as f:
                    setting = pkl.load(f)
                    self.autoLockTime = setting.autoLockTime
                    self.showToolTips = setting.showToolTips
                    self.showLineIndex = setting.showLineIndex
                    self.applyBeforeDel = setting.applyBeforeDel
                    self.useRegExpFilite = setting.useRegExpFilite
                    self.autoBackup = setting.autoBackup
                    self.ctrlSelect = setting.ctrlSelect
                    self.singalClickSelect = setting.singalClickSelect
            else:
                self.set_default()
        except IOError:
            self.set_default()

    def set_default(self):
        self.autoLockTime = 3
        self.showToolTips = True
        self.showLineIndex = False
        self.applyBeforeDel = True
        self.useRegExpFilite = True
        self.autoBackup = False
        self.ctrlSelect = False
        self.singalClickSelect = True

    def save(self, path):
        if path is None:
            path = dbAbsPath + '.settings'
        with open(path, 'wb') as f:
            pkl.dump(self, f)


class SettingUi(QWidget):
    # 向其它对象广播设置
    broadcastSettingSignal = pyqtSignal(Setting)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_settingDialog()
        self.ui.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)
        self.path = dbAbsPath + '.settings'
        self.setting = Setting(self.path)
        self.show_setting()
        # 槽函数连接
        self.ui.pbt_save.clicked.connect(self.save_settings)
        self.ui.pbt_cancel.clicked.connect(self.close)

    def show_setting(self):
        self.ui.cb_showToolTips.setChecked(self.setting.showToolTips)
        self.ui.cb_showLineIndex.setChecked(self.setting.showLineIndex)
        self.ui.cb_deleteTips.setChecked(self.setting.applyBeforeDel)
        self.ui.cb_useRegExpSearch.setChecked(self.setting.useRegExpFilite)
        self.ui.cb_autoBackup.setChecked(self.setting.autoBackup)
        self.ui.sb_autoLockTime.setValue(self.setting.autoLockTime)
        self.ui.cb_mouseClickSelect.setChecked(self.setting.singalClickSelect)
        self.ui.cb_pushCtrl.setChecked(self.setting.ctrlSelect)

    def save_settings(self):
        self.setting.autoLockTime = self.ui.sb_autoLockTime.value()
        self.setting.showToolTips = self.ui.cb_showToolTips.isChecked()
        self.setting.showLineIndex = self.ui.cb_showLineIndex.isChecked()
        self.setting.applyBeforeDel = self.ui.cb_deleteTips.isChecked()
        self.setting.autoBackup = self.ui.cb_autoBackup.isChecked()
        self.setting.useRegExpFilite = self.ui.cb_useRegExpSearch.isChecked()
        self.setting.ctrlSelect = self.ui.cb_pushCtrl.isChecked()
        self.setting.singalClickSelect = self.ui.cb_mouseClickSelect.isChecked()
        # 保存设置
        self.setting.save(self.path)
        # 广播发送设置
        self.broadcastSettingSignal.emit(self.setting)
        self.tip = TipUi('保存成功')
        self.tip.show()
        self.close()

    def closeEvent(self, event):
        # 如果设置没有保存
        if self.setting.autoLockTime != self.ui.sb_autoLockTime.value() or \
            self.setting.showToolTips != self.ui.cb_showToolTips.isChecked() or \
            self.setting.showLineIndex != self.ui.cb_showLineIndex.isChecked() or \
            self.setting.applyBeforeDel != self.ui.cb_deleteTips.isChecked() or \
            self.setting.autoBackup != self.ui.cb_autoBackup.isChecked() or \
            self.setting.useRegExpFilite != self.ui.cb_useRegExpSearch.isChecked() or \
            self.setting.singalClickSelect != self.ui.cb_mouseClickSelect.isChecked() or \
           self.setting.ctrlSelect != self.ui.cb_pushCtrl.isChecked():

            pbt = MessageBox.warning(self, '保存设置', '设置修改后尚未保存，\n关闭后将会丢失，是否保存？', MessageBox.YES | MessageBox.NO | MessageBox.CANCEL, MessageBox.YES)
            if pbt == MessageBox.YES:
                self.save_settings()
                event.accept()
            elif pbt == MessageBox.CANCEL:
                event.ignore()
            else:
                event.accept()

    def showEvent(self, event):
        self.show_setting()
