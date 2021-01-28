from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QSize


class MyMessageBox(QMessageBox):
    def __init__(self, parent, title, text, button, icon):
        super().__init__(parent)
        self.setText(text)
        self.setIcon(icon)
        self.setFixedSize(QSize(3000, 300))
        # self.setBaseSize(QSize(500, 500))
        self.setWindowTitle(title)
        self.setStandardButtons(button)
        self.setStyleSheet("""
            QPushButton {
                border-style:none;
                padding:5px;
                border-radius:8px;
                color:#FFFFFF;
                background:#34495E;
                border:2px solid #34495E;
                font-family:Microsoft YaHei UI;
                font-size:15px;
                font-style:bold;
            }
            QPushButton:hover {
                color:#4E6D8C;
                background:#F0F0F0;
            }
            QPushButton:pressed {
                color:#2D3E50;
                background:#B8C6D1;
            }
        """)
    
    def resizeEvent(self, event):
        ...
