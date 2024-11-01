from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import Qt

class BaseButton(QPushButton):
    """基础按钮,控制按钮的基本样式，有效避免重复代码
        1 初始化大小
        2 初始化部件
        3 初始化样式
        """
    def __init__(self):
        super().__init__()
        self.init_size()
        self.init_self()
        self.init_background()

    def init_size(self):
        """初始化大小"""
        self.setMinimumHeight(90)
        self.setMaximumWidth(150)
    
    def init_self(self):
        """初始化部件"""

    def init_background(self):
        """初始化样式"""
        self.setStyleSheet("""
                color: red;
                border-radius: 10px;
            """)