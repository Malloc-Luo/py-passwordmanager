# -*- coding:utf-8 -*-

from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtCore import pyqtSignal, Qt
from gui.Ui_GenPasswordUi import Ui_GenPassword
from random import randint, shuffle
import secrets, string
import sys


class GenPasswordUi(QWidget):
    sendSignel = pyqtSignal(str)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_GenPassword()
        self.ui.setupUi(self)
        self.setAttribute(Qt.WA_DeleteOnClose, True)
        self.setWindowModality(Qt.ApplicationModal)
        self.ui.pbt_gen.clicked.connect(self.gen_pswd)
        self.ui.pbt_sure.clicked.connect(self.sure_pressed)
        self.ui.cbx_char.clicked.connect(self.check_checked_box)
        self.ui.cbx_digital.clicked.connect(self.check_checked_box)
        self.ui.cbx_lowercase.clicked.connect(self.check_checked_box)
        self.ui.cbx_uppercase.clicked.connect(self.check_checked_box)

    def sure_pressed(self):
        self.sendSignel.emit(self.genPswd)
        self.close()

    def check_checked_box(self):
        state = self.ui.cbx_char.isChecked() or self.ui.cbx_digital.isChecked() or self.ui.cbx_lowercase.isChecked() or self.ui.cbx_uppercase.isChecked()
        self.ui.pbt_gen.setDisabled(not state)

    def gen_pswd(self):
        # 密码随机长度
        self.content, pswd = {}, []
        maxl = self.ui.spb_maxl.value()
        minl = self.ui.spb_minl.value()
        self.length = randint(min(maxl, minl), max(maxl, minl))
        self.content['uppercase'] = self.ui.cbx_uppercase.isChecked()
        self.content['lowercase'] = self.ui.cbx_lowercase.isChecked()
        self.content['digital'] = self.ui.cbx_digital.isChecked()
        self.content['char'] = self.ui.cbx_char.isChecked()
        # 选中的项数
        kind = sum(self.content.values())

        lengths = self.split_number(self.length, kind)
        index = 0
        for item in self.content.items():
            if item[1] == True:
                if item[0] == 'uppercase':
                    pswd += [secrets.choice(string.ascii_uppercase) for i in range(lengths[index])]
                elif item[0] == 'lowercase':
                    pswd += [secrets.choice(string.ascii_lowercase) for i in range(lengths[index])]
                elif item[0] == 'digital':
                    pswd += [secrets.choice(string.digits) for i in range(lengths[index])]
                elif item[0] == 'char':
                    pswd += [secrets.choice(['.', '-', '@']) for i in range(lengths[index])]
                index += 1
        shuffle(pswd)
        self.genPswd = ''.join(pswd)
        self.ui.tb_brower.setText(self.genPswd)
        self.ui.pbt_sure.setEnabled(True)

    def split_number(self, length, kind):
        lengths, rlength = [], length
        if kind == 1:
            return [length]
        while True:
            if kind == 1:
                break
            l = randint(1, length - kind + 1)
            lengths.append(l)
            kind, length = kind - 1, length - l
        lengths.append(rlength - sum(lengths))
        return lengths


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = GenPasswordUi()
    w.show()
    sys.exit(app.exec_())