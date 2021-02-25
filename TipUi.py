from gui.Ui_tips import Ui_Dialog
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import Qt, QTimer, QRect
from WidgetEffect import set_shadow_effect
import sys


def static_vars(**kwargs):
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func
    return decorate


# NormalStyleSheet = "background-color:rgb(37, 255, 237);\nborder-style:none;\npadding:8px;\nborder-radius:25px;"
NormalStyleSheet = "background-color:#ffffff;\nborder-style:none;\npadding:8px;\nborder-radius:25px;"
WarningStyleSheet = "background-color:rgb(255, 255, 127);\ncolor:rgb(255, 0, 127);\nborder-style:none;\npadding:8px;\nborder-radius:25px;"
ErrorStyleSheet = """background-color:qlineargradient(spread:pad, x1:0.368421, y1:0, x2:0.389, y2:1, stop:0 rgba(255, 85, 127, 255), stop:1 rgba(255, 170, 255, 255));
                    color:rgb(0, 0, 0);\nborder-style:none;\npadding:8px;\nborder-radius:25px;"""


class TipUi(QDialog):
    """ 气泡弹窗界面\n
    在界面上弹出一个气泡，非模态，显示时常2500ms，在前800ms透明度为1.0，后1700ms透明度线性降低\n
    后续扩展：动态上升、移动，改变颜色。
    仅用于提示
    Args:\n
        text: 显示气泡的文本
        parent: 父窗口
    """
    NORMAL = 0x00
    WARNING = 0x01
    ERROR = 0x02

    def __init__(self, text='', style=NORMAL, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.timer = QTimer()

        desktop = QApplication.desktop()
        self.setGeometry(QRect(int(desktop.width() / 2 - 75), int(desktop.height() * 0.3), 167, 70))
        self.ui.pushButton.setText(text)
        set_shadow_effect(self.ui.pushButton, radius=20)
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.FramelessWindowHint | Qt.Tool | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setAttribute(Qt.WA_QuitOnClose, True)
        styleSheet = {TipUi.NORMAL: NormalStyleSheet, TipUi.WARNING: WarningStyleSheet, TipUi.ERROR: ErrorStyleSheet}
        self.setStyleSheet(styleSheet[style])
        self.windosAlpha = 0
        # 启动定时器，周期25毫秒
        self.timer.timeout.connect(self.hide_windows)
        self.timer.start(25)

    def hide_windows(self):
        self.timer.start(25)
        if self.windosAlpha <= 30:
            self.setWindowOpacity(1.0)
        else:
            self.setWindowOpacity(1.882 - 0.0294 * self.windosAlpha)
        self.windosAlpha += 1
        if self.windosAlpha >= 63:
            self.close()

    @staticmethod
    @static_vars(tip=None)
    def show_tip(text, style=NORMAL):
        TipUi.show_tip.tip = TipUi(text, style)
        TipUi.show_tip.tip.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    TipUi.show_tip('Hello world')
    sys.exit(app.exec_())
