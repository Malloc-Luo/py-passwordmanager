# -*- coding:utf-8 -*-
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtGui import QHoverEvent, QMouseEvent, QDesktopServices
from PyQt5.QtCore import QObject, QUrl, Qt
from gui.Ui_About import Ui_Dialog
from TipUi import TipUi
import requests, re
import sys


class AboutUi(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.tip = None
        self.version = '0.10.0'
        self.setAttribute(Qt.WA_DeleteOnClose, True)
        self.ui.pbt_code.clicked.connect(self.open_source_code_website)
        self.ui.pbt_update.clicked.connect(self.check_version)
        self.ui.label.setText('version ' + self.version)

    def open_source_code_website(self):
        QDesktopServices.openUrl(QUrl('https://github.com/Malloc-Luo/py-passwordmanager'))
        self.close()

    def check_version(self):
        r = None
        try:
            r = requests.get('https://api.github.com/repos/Malloc-Luo/py-passwordmanager/releases/latest')
        except:
            self.tip = TipUi('网络错误')
            self.tip.show()
        if 'tag_name' in r.json().keys():
            version = r.json()['tag_name']
            self.compare_version(version)
        else:
            self.tip = TipUi('无新版本可用')
            self.show()

    def compare_version(self, version):
        versionNow = [int(s) for s in self.version.split('.')]
        versionGet = [int(s) for s in version.split('.')]
        # 两个版本的差值
        diff = list(map(lambda x, y:x - y, versionNow, versionGet))
        # 版本相同
        if version == self.version:
            self.tip = TipUi('已是最新版本')
        elif diff[0] < 0 or (diff[0] == 0 and diff[1] < 0) or (diff[0] == 0 and diff[1] == 0 and diff[2] < 0):
            self.tip = TipUi('有新版本可用')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = AboutUi()
    w.show()
    sys.exit(app.exec_())