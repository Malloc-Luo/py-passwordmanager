# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QHeaderView, QMenu, QAction, QToolTip, QShortcut
from PyQt5.QtCore import Qt, pyqtSignal, QEvent, QObject
from PyQt5.QtGui import QIcon, QCursor, QFont, QKeySequence
from gui.Ui_MainGUI import Ui_Form
from WidgetEffect import set_shadow_effect
from AddItemUi import AddItemUi
from UserItem import UserItem
from Setting import Setting, SettingUi
from MessageBox import MessageBox
from AboutUi import AboutUi
from Common import read_qss
from TipUi import TipUi
import operate_password as op
from Operate import Operate, Stack
import copy
import sys

NOTLINE = -1


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

    # 排序模式
    class SortMod:
        byDefault = 0x00
        byName    = 0x01
        byAccount = 0x02
        byEmail   = 0x04

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
        self.ui.le_filiter.installEventFilter(self)
        # 记录用户操作，使用栈记录，可以用于撤回信息
        self.operateStack = Stack()
        self.redoStack = Stack()
        # 是否在进行undo或者redo操作
        self.inDoOperate = False
        self.sortMod = self.SortMod.byDefault
        self.sortDirct = Qt.AscendingOrder
        self.initGetSetting = True

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
        self.ui.table.horizontalHeader().sectionClicked.connect(self.horizontal_header_clicked)
        self.ui.table.horizontalHeader().sortIndicatorChanged.connect(self.force_recover_sort)

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
        self.ui.table.verticalHeader().setStyleSheet(
            "QHeaderView::section{\n"
            "   background:#F8F8F8;\n"
            "   padding:1px;\n"
            "   margin:4px;\n"
            "   color:#000000;\n"
            "   border:2px solid #5E83AA;\n"
            "   border-radius:13px;\n"
            "}")
        # 设置快捷键
        QShortcut('Ctrl+Z', self, self.action_undo)
        QShortcut('Ctrl+Y', self, self.action_redo)

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
        if row != NOTLINE:
            ID = self.ui.table.item(row, 0).text()
            return ID
        return None

    def get_row_by_id(self, ID: str) -> int:
        # 通过项目的ID查找所在行
        for index in range(self.ui.table.rowCount()):
            if ID == self.ui.table.item(index, 0).text():
                return index
        else:
            return NOTLINE

    def set_plaintext_visible(self, r, isvisible):
        # 获取选中行的id
        self.ui.table.cellChanged.disconnect(self.edit_item)
        ID = self.get_selected_id()
        if ID is not None:
            # 设置特定行的密码明文是否可见
            if isvisible is True:
                self.ui.table.item(r, 3).setText(op.decrypt_password(self.itemList[ID].password, self.adminPassword))
            else:
                self.ui.table.item(r, 3).setText('******')
        self.ui.table.cellChanged.connect(self.edit_item)

    # 对象内部槽函数
    # 界面按钮响应，调用子窗口

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
    # 复制账号、密码、邮箱电话、撤回操作、重新操作

    def action_copy(self):
        action = {'复制账号': 2, '复制密码': 3, '复制邮箱/电话': 4}[self.sender().text()]
        row = self.ui.table.currentRow()
        if row != NOTLINE:
            if action == 3:
                ID = self.ui.table.item(row, 0).text()
                self.write_into_clipboard(op.decrypt_password(self.itemList[ID].password, self.adminPassword))
            else:
                self.write_into_clipboard(self.ui.table.item(row, action).text())
            TipUi.show_tip(self.sender().text())

    def action_undo(self):
        operate = self.operateStack.pop()
        self.redoStack.push(operate)
        self.inDoOperate = True
        # 撤回添加操作，相反操作为删除对应项
        if operate.op == Operate.ADD:
            self.deleteItemSignal.emit(operate.item.id)
        # 撤回删除操作，相反操作为添加对应项
        elif operate.op == Operate.DELETE:
            self.addItemSignal.emit(operate.item)
        # 编辑操作恢复为原来的项
        elif operate.op == Operate.EDIT:
            self.modifySignal.emit(operate.id, operate.title, operate.value)

    def action_redo(self):
        operate = self.redoStack.pop()
        self.operateStack.push(operate)
        self.inDoOperate = True
        # 恢复操作，恢复之前的动作，按照op做就行了
        if operate.op == Operate.ADD:
            self.addItemSignal.emit(operate.item)
        elif operate.op == Operate.DELETE:
            self.deleteItemSignal.emit(operate.item.id)
        elif operate.op == Operate.EDIT:
            self.modifySignal.emit(operate.id, operate.title, operate.currentValue)

    def action_sort(self):
        if self.sortDirct == Qt.DescendingOrder:
            self.sortDirct = Qt.AscendingOrder
        elif self.sortDirct == Qt.AscendingOrder:
            self.sortDirct = Qt.DescendingOrder
        try:
            index = {u'默认排序': 0, u'按名称排序': 1, u'按账号排序': 2, u'按邮箱排序': 4}[self.sender().text()]
        except IndexError:
            index = self.SortMod.byDefault
        self.sortMod = index
        self.ui.table.sortItems(index, self.sortDirct)

    def action_cancel_line(self):
        row = self.ui.table.currentRow()
        if row != NOTLINE:
            self.set_plaintext_visible(row, False)
        self.ui.table.setCurrentItem(None)

    def create_right_menu(self):
        # 创建右键菜单
        self.tableMenu = QMenu(self)
        self.actionCopyAccount = QAction(QIcon(':/mainui/icon/account.png'), u'复制账号', self)
        self.actionCopyPassword = QAction(QIcon(':/mainui/icon/password.png'), u'复制密码', self)
        self.actionCopyEmail = QAction(QIcon(':/mainui/icon/connect.png'), u'复制邮箱/电话', self)
        self.actionUndo = QAction(QIcon(':/mainui/icon/undo.png'), u'撤回操作', self)
        self.actionRedo = QAction(QIcon(':/mainui/icon/redo.png'), u'恢复操作', self)
        self.actionCancelLine = QAction(QIcon(':/mainui/icon/cancelLine.png'), u'取消选中', self)
        self.actionDelete = QAction(QIcon(':/mainui/icon/delete1.png'), u'删除', self)
        self.actionAdd = QAction(QIcon(':/mainui/icon/add.png'), u'新建', self)
        self.actionSortDefault = QAction(QIcon(''), u'默认排序')
        self.actionSortDefault.setCheckable(True)
        self.actionSortByAccount = QAction(QIcon(''), u'按账号排序')
        self.actionSortByAccount.setCheckable(True)
        self.actionSortByName = QAction(QIcon(''), u'按名称排序')
        self.actionSortByName.setCheckable(True)
        self.actionSortByEmail = QAction(QIcon(''), u'按邮箱排序')
        self.actionSortByEmail.setCheckable(True)
        [self.actionSortDefault, self.actionSortByName, self.actionSortByAccount, ..., self.actionSortByEmail][self.sortMod].setChecked(True)
        # 添加按键到右键菜单
        self.tableMenu.addAction(self.actionCopyAccount)
        self.tableMenu.addAction(self.actionCopyPassword)
        self.tableMenu.addAction(self.actionCopyEmail)
        self.tableMenu.addAction(self.actionUndo)
        self.tableMenu.addAction(self.actionRedo)
        self.actionSort = self.tableMenu.addMenu(QIcon(':/mainui/icon/order.png'), u'排序方式')
        self.actionSort.addActions([
            self.actionSortDefault, self.actionSortByName,
            self.actionSortByAccount, self.actionSortByEmail
        ])
        self.tableMenu.addAction(self.actionCancelLine)
        self.tableMenu.addAction(self.actionDelete)
        self.tableMenu.addAction(self.actionAdd)
        self.tableMenu.popup(QCursor.pos())
        # 检查是否可用
        row = self.ui.table.currentRow()
        self.actionCopyAccount.setDisabled(row == NOTLINE)
        self.actionCopyEmail.setDisabled(row == NOTLINE)
        self.actionCopyPassword.setDisabled(row == NOTLINE)
        self.actionDelete.setDisabled(row == NOTLINE)
        self.actionCancelLine.setDisabled(row == NOTLINE)
        self.actionUndo.setDisabled(self.operateStack.empty())
        self.actionRedo.setDisabled(self.redoStack.empty())
        self.actionSort.setDisabled(self.ui.table.rowCount() == 0)
        # 获取堆栈顶部的项的标签
        if self.operateStack.empty() is False:
            top = self.operateStack.get_top()
            self.actionUndo.setText(u'撤回「%s」' % top.op)
        if self.redoStack.empty() is False:
            top = self.redoStack.get_top()
            self.actionRedo.setText(u'恢复「%s」' % top.op)
        # 连接槽函数
        self.actionDelete.triggered.connect(self.remove_line)
        self.actionAdd.triggered.connect(self.add_item_ui)
        self.actionUndo.triggered.connect(self.action_undo)
        self.actionRedo.triggered.connect(self.action_redo)
        self.actionCopyAccount.triggered.connect(self.action_copy)
        self.actionCopyPassword.triggered.connect(self.action_copy)
        self.actionCopyEmail.triggered.connect(self.action_copy)
        self.actionSortDefault.triggered.connect(self.action_sort)
        self.actionSortByName.triggered.connect(self.action_sort)
        self.actionSortByAccount.triggered.connect(self.action_sort)
        self.actionSortByEmail.triggered.connect(self.action_sort)
        self.actionCancelLine.triggered.connect(self.action_cancel_line)

    def horizontal_header_clicked(self, index):
        if index not in {3, 5}:
            self.sortMod = {1: 1, 2: 2, 4: 4}[index]

    def force_recover_sort(self, index, order):
        if index in {3, 5}:
            self.ui.table.horizontalHeader().setSortIndicator(self.sortMod, self.sortDirct)
        else:
            # self.sortDirct = order
            ...

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

    def remove_line(self):
        # 点击删除按钮，发送删除信号
        if self.ui.table.currentRow() != NOTLINE:
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
        # cr != NOTLINE 只出现一行的情况
        if cr != NOTLINE and (self.ctrlPressed is True or self.setting.ctrlSelect is False):
            if pr != NOTLINE and pr != cr:
                self.set_plaintext_visible(pr, False)
            self.set_plaintext_visible(cr, True)
        else:
            self.set_plaintext_visible(cr, False)

    def add_line_item(self, userItem: UserItem):
        # 新建项目，在这里加载key
        # 添加的时候禁用排序，否则后面会混乱
        self.ui.table.setSortingEnabled(False)
        self.itemList[userItem.id] = userItem.load_key(self.adminPassword)
        index = self.ui.table.rowCount()
        self.ui.table.setRowCount(index + 1)
        # 内容缓存
        contents = [userItem.id, userItem.name, userItem.account, '******', userItem.email_or_phone, userItem.note]
        # 显示内容，以及设置中间对齐
        for i in range(0, 5 + 1):
            self.ui.table.setItem(index, i, QTableWidgetItem(contents[i]))
            self.ui.table.item(index, i).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        font = QFont()
        font.setFamily('consolas')
        font.setPointSizeF(9.8)
        headerItem = QTableWidgetItem(str(index + 1))
        headerItem.setFont(font)
        self.ui.table.setVerticalHeaderItem(index, headerItem)
        self.ui.table.verticalHeaderItem(index).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.ui.table.setSortingEnabled(True)

    def filite_item(self):
        # 筛选项目，当描述不为空时发送
        description = self.ui.le_filiter.text().replace(' ', '')
        if len(description) != 0:
            item = {'全部': '*', '名称': 'name', '账号': 'account', '邮箱/电话': 'email_or_phone', '备注': 'note'}[self.ui.comboBox.currentText()]
            self.filiteSignal.emit(item, description)
        else:
            self.refresh_table()

    def select_edit_item(self, r, c):
        if c == 3:
            self.set_plaintext_visible(r, True)
        self.cellclicked = True

    def edit_item(self, row: int, column: int):
        # 编辑项目槽函数 cellchange信号
        if self.cellclicked is True:
            self.cellclicked = False
            header = {
                1: 'name',
                2: 'account',
                3: 'password',
                4: 'email_or_phone',
                5: 'note'
            }[column]
            ID = self.get_selected_id()
            # 该项内容的缓存
            backup = copy.copy(self.itemList[ID])
            # 前三项不能为空，如果为空则强制恢复
            if len(self.ui.table.item(row, column).text().strip()) == 0 and column in {1, 2, 3}:
                if column == 3:
                    self.ui.table.item(row, column).setText(op.decrypt_password(backup['password'], self.adminPassword))
                else:
                    self.ui.table.item(row, column).setText(backup[column])
            else:
                content = self.ui.table.item(row, column).text()
                # 如果修改的是密码，则加密后再发送
                if column == 3:
                    content = op.encrypt_password(content, self.adminPassword)
                self.modifySignal.emit(ID, header, content)
                self.operateStack.push(Operate(Operate.EDIT, ID, header, backup[column], content))
            if self.setting.ctrlSelect is True and self.ctrlPressed is False:
                self.set_plaintext_visible(row, False)
        else:
            self.cellclicked = False

    # 对外的槽函数
    # 在main.py里连接别的窗口的信号

    def get_add_res(self, issuccess: bool, userItem: UserItem):
        # 获取添加的结果，如果添加成功则为真，否则为False
        if issuccess is True:
            self.add_line_item(userItem)
            # 放到记录里
            if self.inDoOperate is False:
                self.operateStack.push(Operate(Operate.ADD, userItem))
                TipUi.show_tip('添加成功')
            else:
                self.inDoOperate = False
        else:
            MessageBox.error(self, u'添加项目', u'添加时发生错误，请重启程序再次尝试', MessageBox.CLOSE)
            sys.exit()

    def get_delete_res(self, issuccess: bool, ID: str):
        # 删除成功信号
        if issuccess is True:
            item = self.itemList.pop(ID)
            row = self.get_row_by_id(ID)
            if row != NOTLINE:
                self.ui.table.removeRow(row)
            # 在进行常规的删除操作
            if self.inDoOperate is False:
                self.operateStack.push(Operate(Operate.DELETE, item))
                TipUi.show_tip('删除成功')
            else:
                self.inDoOperate = False
        else:
            MessageBox.error(self, u'删除项目', u'删除时发生错误，请重启程序再次尝试', MessageBox.CLOSE)
            sys.exit()

    def get_edit_res(self, flag: bool, ID: str, header: str, value: str):
        if flag is True:
            self.itemList[ID][header] = value
            row = self.get_row_by_id(ID)
            column = {'name': 1, 'account': 2, 'password': 3, 'email_or_phone': 4, 'note': 5}[header]
            if column == 3:
                self.ui.table.item(row, column).setText(op.decrypt_password(value, self.adminPassword))
            else:
                self.ui.table.item(row, column).setText(value)
        else:
            MessageBox.error(self, u'编辑项目', u'编辑时数据库发生错误，请重启程序再次尝试', MessageBox.CLOSE)
            sys.exit()

    def get_filite_id(self, luserItemID: list):
        # 获取过滤结果元素的id列表
        # 清空列表
        self.ui.table.clearContents()
        self.ui.table.setRowCount(0)
        for ID in luserItemID:
            self.add_line_item(self.itemList[ID])

    def load_items(self, duserItem: dict):
        # 加载所有项，参数为所有项目组成的字典，key为ID
        self.ui.table.clearContents()
        self.ui.table.setRowCount(0)
        self.itemList = duserItem
        for v in self.itemList.values():
            self.add_line_item(v)

    def get_admin_password(self, adminPassword: str):
        # 获取管理员密码明文
        self.adminPassword = adminPassword
        self.loadItemSignal.emit()

    def get_setting(self, setting: Setting):
        # 获取设置信息，在设置窗口点击保存或者启动时加载设置项
        self.setting = setting
        # 决定行号是否可见
        self.ui.table.verticalHeader().setVisible(self.setting.showLineIndex)
        if len(self.ui.le_filiter.text().replace(' ', '')) == 0:
            self.refresh_table()
        if self.initGetSetting is True:
            self.resize(self.setting.wSize[0], self.setting.wSize[1])
            self.initGetSetting = False

    def eventFilter(self, widget, event):
        if widget == self.ui.le_filiter:
            if event.type() == QEvent.FocusIn:
                set_shadow_effect(widget)
            elif event.type() == QEvent.FocusOut:
                set_shadow_effect(widget, visible=False)
        return QObject.eventFilter(self, widget, event)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Control:
            self.ctrlPressed = True
            if self.ui.table.currentRow() != NOTLINE and self.setting.ctrlSelect is True:
                self.set_plaintext_visible(self.ui.table.currentRow(), True)
        elif event.key() == Qt.Key_Alt:
            self.action_cancel_line()

    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_Control:
            self.ctrlPressed = False
            if self.ui.table.currentRow() != NOTLINE and self.setting.ctrlSelect is True:
                self.set_plaintext_visible(self.ui.table.currentRow(), False)

    def closeEvent(self, event):
        self.initGetSetting = True
        self.setting.wSize = (self.size().width(), self.size().height())
        self.setting.save()
        if self.ui_aboutW is not None:
            self.ui_aboutW.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainGUI()
    w.show()
    sys.exit(app.exec_())
