# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTableWidgetItem, QHeaderView, QMessageBox
from PyQt5.QtCore import Qt, pyqtSignal
from gui.Ui_MainGUI import Ui_Form
from AddItemUi import AddItemUi
from UserItem import UserItem
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

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.addItemUi = AddItemUi()
        self.itemList = []
        # 设置表格
        self.set_tableWidget()
        self.init_connect()

    def init_connect(self):
        self.ui.pbt_add.clicked.connect(self.add_item_ui)
        self.ui.pushButton.clicked.connect(self.remove_line)
        self.ui.le_filiter.cursorPositionChanged.connect(self.filite_item)

    def set_tableWidget(self):
        self.ui.table.setColumnHidden(0, True)
        self.ui.table.setColumnHidden(6, True)
        self.ui.table.setColumnHidden(7, True)
        width = self.ui.table.width()
        for i in range(1, 6):
            self.ui.table.horizontalHeader().setSectionResizeMode(i, QHeaderView.ResizeToContents)

    # 内部的槽函数
    def add_item_ui(self):
        """ 点击添加按钮槽函数      
        先获取填写的信息，而后向数据库发送信息，添加成功则显示在tableWidget中
        """
        # 初始添加页面的ui
        self.addItemUi = AddItemUi()
        self.addItemUi.userItemSignal.connect(self.get_new_line)
        self.addItemUi.show()

    def get_new_line(self, userItem:UserItem):
        """ self signal slot
        """
        # 向数据库发送添加的信号，添加到数据库中
        self.addItemSignal.emit(UserItem)
        self.add_line_item(userItem)

    def remove_line(self):
        r = self.ui.table.currentRow()
        self.ui.table.removeRow(r)

    def view_item(self):
        print('Hello')

    def add_line_item(self, userItem:UserItem):
        self.itemList.append(userItem)
        index = self.ui.table.rowCount()
        self.ui.table.setRowCount(index + 1)
        self.ui.table.setItem(index, 0, QTableWidgetItem(userItem.id))
        self.ui.table.setItem(index, 1, QTableWidgetItem(userItem.name))
        self.ui.table.item(index, 1).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.ui.table.setItem(index, 2, QTableWidgetItem(userItem.account))
        self.ui.table.item(index, 2).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.ui.table.setItem(index, 3, QTableWidgetItem('******'))
        self.ui.table.item(index, 3).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.ui.table.setItem(index, 4, QTableWidgetItem(userItem.email_or_phone))
        self.ui.table.item(index, 4).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.ui.table.setItem(index, 5, QTableWidgetItem(userItem.note))
        self.ui.table.item(index, 5).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

    def filite_item(self):
        description = self.ui.le_filiter.text().replace(' ', '')
        if len(description) != 0:
            item = {'全部':'*', '名称':'name', '账号':'account', '邮箱/电话':'email_or_phone'}[self.ui.comboBox.currentText()]
            self.filiteSignal.emit(item, description)
            print(item, description)

    # 对外的槽函数
    def get_add_res(self, issuccess:bool):
        ...

    def get_delete_res(self, issuccess:bool):
        ...

    def get_filite_id(self, luserItemID:list):
        # 清空列表
        self.ui.table.clearContents()
        # 将符合条件的列表添加进到table上
        for userItem in self.itemList:
            if userItem.id in luserItemID:
                self.add_line_item(userItem)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainGUI()
    w.show()
    sys.exit(app.exec_())
