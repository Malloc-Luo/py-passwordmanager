# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTableWidgetItem, QHeaderView, QMessageBox
from PyQt5.QtCore import Qt
from gui.Ui_MainGUI import Ui_Form
from AddItemUi import AddItemUi
from UserItem import UserItem
import sys


class ViewPushButton(QPushButton):
    ...


class MainGUI(QWidget):
    """ 主界面窗口，继承QWidget，ui为Ui_Form
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.addItemUi = AddItemUi()
        self.itemList = []
        # 设置表格
        self.set_tableWidget()
        self.init_connect()
        # 子窗口ui
        self.add_line_item(UserItem('12357', 'QQ', '2423049596', '242242222222222', '132'))
        self.add_line_item(UserItem('12359', '微信', '24230445646465469596', '456', '132'))

    def init_connect(self):
        self.ui.pbt_add.clicked.connect(self.add_item_ui)
        # 删除键
        self.ui.pushButton.clicked.connect(self.remove_line)

    def add_item_ui(self):
        """ add pushbutton slot
        """
        self.addItemUi = AddItemUi()
        self.addItemUi.userItemSignal.connect(self.get_new_line)
        self.addItemUi.show()

    def get_new_line(self, userItem:UserItem):
        """ self signal slot
        """
        self.add_line_item(userItem)

    def remove_line(self):
        r = self.ui.table.currentRow()
        self.ui.table.removeRow(r)

    def set_tableWidget(self):
        self.ui.table.setColumnHidden(0, True)
        self.ui.table.setColumnHidden(6, True)
        self.ui.table.setColumnHidden(7, True)
        width = self.ui.table.width()
        for i in range(1, 6):
            self.ui.table.horizontalHeader().setSectionResizeMode(i, QHeaderView.ResizeToContents)

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainGUI()
    w.show()
    sys.exit(app.exec_())
