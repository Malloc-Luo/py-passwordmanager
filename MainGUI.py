# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QHeaderView, QMenu, QAction, QToolTip
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QIcon, QCursor
from gui.Ui_MainGUI import Ui_Form
from AddItemUi import AddItemUi
from UserItem import UserItem
from Setting import Setting, SettingUi
from MessageBox import MessageBox
from AboutUi import AboutUi
from Common import read_qss
from TipUi import TipUi
import operate_password as op
import sys


class MainGUI(QWidget):
    """ 主界面窗口，继承QWidget，ui为Ui_Form
    """
    # 加载信号，无参数
    loadItemSignal = pyqtSignal()
    # 删除信号，参数为项目的id
    deleteItemSignal = pyqtSignal(str)
    # 添加信号，参数为UserItem
    addItemSignal = pyqtSignal(UserItem)
    # 修改信号，参数为ID，项目，和值
    modifySignal = pyqtSignal(str, str, str)
    # 筛选信号，参数为项目和筛选条件
    filiteSignal = pyqtSignal(str, str)
    # 打开子窗口
    openSubWSignal = pyqtSignal(bool)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # 构造ui界面
        self.addItemUi = AddItemUi()
        self.ui_settingW = SettingUi()
        self.ui_aboutW = AboutUi()
        # 项目字典，key是id，value为userItem对象
        self.itemList = {}
        # 单元格是否双击选中
        self.cellclicked = False
        # ctrl键是否被按下
        self.ctrlPressed = False
        # 设置表格的样式和属性
        self.set_tableWidget()
        # 开启鼠标捕获，在表格里显示tooltips
        self.ui.table.setMouseTracking(True)
        # 槽函数初始化连接（主要的）
        self.init_connect()

    def init_connect(self):
        self.ui.pbt_add.clicked.connect(self.add_item_ui)
        self.ui.pushButton.clicked.connect(self.remove_line)
        self.ui.le_filiter.cursorPositionChanged.connect(self.filite_item)
        self.ui.comboBox.currentTextChanged.connect(self.filite_item)
        self.ui.table.cellChanged.connect(self.edit_item)
        self.ui.table.cellDoubleClicked.connect(self.select_edit_item)
        self.ui.table.currentCellChanged.connect(self.view_item_changed)
        self.ui.pbt_setting.clicked.connect(self.call_setting_ui)
        self.ui.pbt_about.clicked.connect(self.call_about_ui)
        # 添加右键菜单
        self.ui.table.customContextMenuRequested.connect(self.create_right_menu)
        self.ui.table.cellEntered.connect(self.set_tool_tips)
        # 获取设置
        self.ui_settingW.broadcastSettingSignal.connect(self.get_setting)

    def set_tableWidget(self):
        self.ui.table.setColumnHidden(0, True)
        self.ui.table.setColumnHidden(6, True)
        self.ui.table.setColumnHidden(7, True)
        self.ui.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.ui.table.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.ui.table.horizontalHeader().setSectionResizeMode(3, QHeaderView.Stretch)
        self.ui.table.horizontalHeader().setSectionResizeMode(4, QHeaderView.Stretch)
        self.ui.table.horizontalHeader().setSectionResizeMode(5, QHeaderView.ResizeToContents)
        self.ui.table.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.ui.table.verticalHeader().setDefaultSectionSize(40)

    def refresh_table(self):
        # 刷新表格，将当前表格清空，发送信号到数据库重新加载
        self.ui.table.clearContents()
        self.ui.table.setRowCount(0)
        # 发送加载信号
        self.loadItemSignal.emit()

    def write_into_clipboard(self, text: str):
        # 写入到计算机剪贴板
        clipboard = QApplication.clipboard()
        clipboard.setText(text)

    def get_selected_id(self) -> str:
        # 获取选中项目的id
        row = self.ui.table.currentRow()
        if row != -1:
            ID = self.ui.table.item(row, 0).text()
            return ID
        return None

    def set_plaintext_visible(self, r, isvisible):
        # 获取选中行的id
        ID = self.get_selected_id()
        if ID is not None:
            # 设置特定行的密码明文是否可见
            if isvisible is True:
                self.ui.table.item(r, 3).setText(op.decrypt_password(self.itemList[ID].password, self.adminPassword))
            else:
                self.ui.table.item(r, 3).setText('******')

    ##################################################
    # 对象内部槽函数
    # 界面按钮响应，调用子窗口
    ##################################################
    def call_setting_ui(self):
        # 点击设置按钮，调用设置界面
        self.ui_settingW.show()

    def call_about_ui(self):
        # 点击关于按钮，调用关于界面
        self.ui_aboutW.show()

    def set_tool_tips(self, r, c):
        # 设置tooltips，鼠标悬浮在cell上，选择模式
        item = self.ui.table.item(r, c)
        if item is not None and self.setting.showToolTips is True:
            QToolTip.showText(QCursor.pos(), item.text())
        # 设置项目是否单击选中，如果是则单击选中，否则悬浮选中
        if item is not None and self.setting.singalClickSelect is False:
            self.ui.table.selectRow(r)

    # 点击右键菜单项目槽函数
    def action_copy_account(self):
        # 点击右键“复制账号”
        self.tip = TipUi('复制账号成功')
        self.tip.show()
        row = self.ui.table.currentRow()
        if row != -1:
            self.write_into_clipboard(self.ui.table.item(row, 2).text())

    def action_copy_password(self):
        # 点击右键“复制密码”
        self.tip = TipUi('复制密码成功')
        self.tip.show()
        row = self.ui.table.currentRow()
        if row != -1:
            self.write_into_clipboard(self.ui.table.item(row, 3).text())

    def action_copy_email(self):
        # 点击右键“复制邮箱/电话”
        self.tip = TipUi('复制邮/电成功')
        self.tip.show()
        row = self.ui.table.currentRow()
        if row != -1:
            self.write_into_clipboard(self.ui.table.item(row, 4).text())

    def create_right_menu(self):
        # 创建右键菜单
        self.tableMenu = QMenu(self)
        self.tableMenu.setStyleSheet(read_qss('gui/src/qss/QMenu.qss'))
        self.actionCopyAccount = QAction(QIcon('gui/src/icon/account.png'), u'复制账号', self)
        self.actionCopyPassword = QAction(QIcon('gui/src/icon/password.png'), u'复制密码', self)
        self.actionCopyEmail = QAction(QIcon('gui/src/icon/connect.png'), u'复制邮箱/电话', self)
        self.actionDelete = QAction(QIcon('gui/src/icon/delete1.png'), u'删除', self)
        self.actionAdd = QAction(QIcon('gui/src/icon/add.png'), u'新建', self)
        # 添加按键到右键菜单
        self.tableMenu.addAction(self.actionCopyAccount)
        self.tableMenu.addAction(self.actionCopyPassword)
        self.tableMenu.addAction(self.actionCopyEmail)
        self.tableMenu.addAction(self.actionDelete)
        self.tableMenu.addAction(self.actionAdd)
        self.tableMenu.popup(QCursor.pos())
        # 检查是否可用
        row = self.ui.table.currentRow()
        self.actionCopyAccount.setDisabled(row == -1)
        self.actionCopyEmail.setDisabled(row == -1)
        self.actionCopyPassword.setDisabled(row == -1)
        self.actionDelete.setDisabled(row == -1)
        # 连接槽函数
        self.actionCopyAccount.triggered.connect(self.action_copy_account)
        self.actionCopyPassword.triggered.connect(self.action_copy_password)
        self.actionCopyEmail.triggered.connect(self.action_copy_email)
        self.actionDelete.triggered.connect(self.remove_line)
        self.actionAdd.triggered.connect(self.add_item_ui)

    def add_item_ui(self):
        # 点击“添加”按钮，调用添加界面
        # 初始添加页面的ui
        self.addItemUi = AddItemUi()
        self.addItemUi.userItemSignal.connect(self.get_new_line)
        self.addItemUi.closeSubWSignal.connect(self.subW_close)
        self.addItemUi.show()
        # 打开子窗口信号
        self.openSubWSignal.emit(True)

    def subW_close(self):
        # 子窗口addItem窗口关闭时发送的信号
        self.openSubWSignal.emit(False)

    def get_new_line(self, userItem: UserItem):
        # 向数据库发送添加的信号，添加到数据库中
        self.addItemSignal.emit(userItem.load_key(self.adminPassword))
        self.add_line_item(userItem)

    def remove_line(self):
        # 点击删除按钮，发送删除信号
        if self.ui.table.currentRow() != -1:
            ID = self.get_selected_id()
            # 如果设置项中删除前提示
            if self.setting.applyBeforeDel is True:
                msg = MessageBox.information(self, '删除选项', '是否删除所选项？', MessageBox.YES | MessageBox.CANCEL)
                if msg == MessageBox.YES:
                    # 发送删除信号，为删除项的ID
                    self.deleteItemSignal.emit(ID)
            else:
                self.deleteItemSignal.emit(ID)

    def view_item_changed(self, cr, cc, pr, pc):
        """ 查看项目变化，只有被选中的行才能显示密码明文，未被选中的显示星号。\n
        对应当前行显示密码明文，上次被选中的行变成星号
        """
        # cr != -1 只出现一行的情况
        if cr != -1 and (self.ctrlPressed is True or self.setting.ctrlSelect is False):
            self.set_plaintext_visible(cr, True)
            if pr != -1 and pr != cr:
                self.set_plaintext_visible(pr, False)
        else:
            self.set_plaintext_visible(cr, False)

    def add_line_item(self, userItem: UserItem):
        # 新建项目，在这里加载key
        self.itemList[userItem.id] = userItem.load_key(self.adminPassword)
        index = self.ui.table.rowCount()
        self.ui.table.setRowCount(index + 1)
        # 内容缓存
        contents = [userItem.id, userItem.name, userItem.account, '******', userItem.email_or_phone, userItem.note]
        # 显示内容，以及设置中间对齐
        for i in range(0, 5 + 1):
            self.ui.table.setItem(index, i, QTableWidgetItem(contents[i]))
            self.ui.table.item(index, i).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

    def filite_item(self):
        # 筛选项目，当描述不为空时发送
        description = self.ui.le_filiter.text().replace(' ', '')
        if len(description) != 0:
            item = {'全部': '*', '名称': 'name', '账号': 'account', '邮箱/电话': 'email_or_phone'}[self.ui.comboBox.currentText()]
            self.filiteSignal.emit(item, description)
        else:
            self.refresh_table()

    def select_edit_item(self, r, c):
        self.cellclicked = True

    def edit_item(self, r: int, c: int):
        # 编辑项目槽函数 cellchange信号
        if self.cellclicked is True:
            self.cellclicked = False
            # 修改的项
            header = {1: 'name', 2: 'account', 3: 'password', 4: 'email_or_phone', 5: 'note'}[c]
            ID = self.get_selected_id()
            # 该项内容的缓存
            backup = [self.itemList[ID].name, self.itemList[ID].account, op.decrypt_password(self.itemList[ID].password, self.adminPassword)]
            # 前三项不能为空
            if len(self.ui.table.item(r, c).text().strip()) == 0 and c in {1, 2, 3}:
                self.ui.table.item(r, c).setText(backup[c - 1])
            else:
                content = self.ui.table.item(r, c).text()
                # 如果修改的是密码，则加密后再发送
                if header == 'password':
                    content = op.encrypt_password(content, self.adminPassword)
                self.modifySignal.emit(ID, header, content)
                self.itemList[ID][header] = content
        else:
            pass

    ##################################################
    # 对外的槽函数
    # 在main.py里连接别的窗口的信号
    ##################################################
    def get_add_res(self, issuccess: bool):
        # 获取添加的结果，如果添加成功则为真，否则为False
        if issuccess is True:
            self.tip = TipUi('添加成功')
            self.tip.show()
        else:
            MessageBox.error(self, u'添加项目', u'添加时发生错误，请重启程序再次尝试', MessageBox.OK)

    def get_delete_res(self, issuccess: bool, ID: str):
        # 删除成功信号
        if issuccess is True:
            self.itemList.pop(ID)
            row = self.ui.table.currentRow()
            if row != -1:
                self.ui.table.removeRow(row)
            # tips弹窗
            self.tip = TipUi('删除成功')
            self.tip.show()
        else:
            MessageBox.error(self, u'删除项目', u'删除时发生错误，请重启程序再次尝试', MessageBox.OK)

    def get_filite_id(self, luserItemID: list):
        # 获取过滤结果元素的id列表
        # 清空列表
        self.ui.table.clearContents()
        self.ui.table.setRowCount(0)
        # 禁用排序
        self.ui.table.setSortingEnabled(False)
        for ID in luserItemID:
            self.add_line_item(self.itemList[ID])
        # 再次开启排序
        self.ui.table.setSortingEnabled(True)

    def load_items(self, duserItem: dict):
        # 加载所有项，参数为所有项目组成的字典，key为ID
        self.ui.table.clearContents()
        self.ui.table.setRowCount(0)
        # 加载项目
        self.itemList = duserItem
        # 添加的时候禁用排序，否则后面会混乱
        self.ui.table.setSortingEnabled(False)
        for v in self.itemList.values():
            self.add_line_item(v)
        self.ui.table.setSortingEnabled(True)

    def get_admin_password(self, adminPassword: str):
        # 获取管理员密码明文
        self.adminPassword = adminPassword
        # 发送信号加载项目
        self.loadItemSignal.emit()

    def get_setting(self, setting:  Setting):
        # 获取设置信息，在设置窗口点击保存或者启动时加载设置项
        self.setting = setting
        # 决定行号是否可见
        self.ui.table.verticalHeader().setVisible(self.setting.showLineIndex)
        # 刷新一次表格
        if len(self.ui.le_filiter.text().replace(' ', '')) == 0:
            self.refresh_table()

    def keyPressEvent(self, event):
        self.ctrlPressed = (event.key() == Qt.Key_Control)
        if self.ui.table.currentRow() != -1 and self.setting.ctrlSelect is True:
            self.set_plaintext_visible(self.ui.table.currentRow(), True)

    def keyReleaseEvent(self, event):
        self.ctrlPressed = not (event.key() == Qt.Key_Control)
        if self.ui.table.currentRow() != -1 and self.setting.ctrlSelect is True:
            self.set_plaintext_visible(self.ui.table.currentRow(), False)

    def closeEvent(self, event):
        if self.ui_aboutW is not None:
            self.ui_aboutW.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainGUI()
    w.show()
    sys.exit(app.exec_())
