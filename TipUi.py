from gui.Ui_tips import Ui_Dialog
from PyQt5.QtWidgets import QWidget, QApplication, QDialog, QGraphicsDropShadowEffect
from PyQt5.QtCore import Qt, QTimer, QRect
import sys
from math import log10


class TipUi(QDialog):
    def __init__(self, text:str, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.timer = QTimer()

        desktop = QApplication.desktop()
        self.setGeometry(QRect(int(desktop.width() / 2 - 75), int(desktop.height() * 0.83), 152, 50))
        self.ui.pushButton.setText(text)
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.FramelessWindowHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setAttribute(Qt.WA_QuitOnClose, True)
        # 设置窗口阴影
        # self.shadow = QGraphicsDropShadowEffect(self)
        # self.shadow.setOffset(10, 10)
        # self.shadow.setBlurRadius(100)
        # self.shadow.setColor(Qt.gray)
        # self.setGraphicsEffect(self.shadow)
        self.windosAlpha = 0

        self.timer.timeout.connect(self.hide_windows)
        self.timer.start(25)

    def hide_windows(self):
        self.timer.start(25)
        if self.windosAlpha <= 32:
            self.setWindowOpacity(1.0)
        else:
            self.setWindowOpacity(1.47 - 0.0147 * self.windosAlpha)
        self.windosAlpha += 1
        if self.windosAlpha >= 118:
            self.close()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = TipUi('复制成功')
    w.show()
    sys.exit(app.exec_())