from gui.Ui_tips import Ui_Dialog
from PyQt5.QtWidgets import QApplication, QDialog, QGraphicsDropShadowEffect
from PyQt5.QtCore import Qt, QTimer, QRect
import sys


class TipUi(QDialog):
    """ 气泡弹窗界面        
    在界面上弹出一个气泡，非模态，显示时常2500ms，在前800ms透明度为1.0，后1700ms透明度线性降低      
    后续扩展：动态上升、移动，改变颜色。
    仅用于提示
    Args:       
        text: 显示气泡的文本
        parent: 父窗口
    """
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
        self.windosAlpha = 0
        # 启动定时器，周期25毫秒
        self.timer.timeout.connect(self.hide_windows)
        self.timer.start(25)

    def hide_windows(self):
        self.timer.start(25)
        if self.windosAlpha <= 30 :
            self.setWindowOpacity(1.0)
        else:
            self.setWindowOpacity(1.882 - 0.0294 * self.windosAlpha)
        self.windosAlpha += 1
        if self.windosAlpha >= 63:
            self.close()

    @staticmethod
    def show_tip(text):
        tip = TipUi(text)
        tip.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # w = TipUi('复制成功')
    # w.show()
    sys.exit(app.exec_())