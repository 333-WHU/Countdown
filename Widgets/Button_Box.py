from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget, QPushButton, QSpinBox,QHBoxLayout,QApplication
from PySide6.QtCore import QTimer, QTime, Qt,QDate
from PySide6.QtGui import QIcon, QFont,QPixmap

from Interfaccia.BaseButton import BaseButton

class UpButton(BaseButton):
    """增加时间按钮"""
    def __init__(self):
        super().__init__()

    def init_size(self):
        """初始化大小"""
        self.setMinimumHeight(90)
        self.setMaximumWidth(150)
    
    def init_self(self):
        """初始化部件"""
        self.printer = QPixmap(".\\Icon\\UpArrow_del.png")

    def init_background(self):
        
        self.layout = QHBoxLayout()
        self.label = QLabel()
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)
        self.label.setPixmap(self.printer)
        self.setStyleSheet("""
                color: red;
                border-radius: 10px;
            """)
        
class DownButton(UpButton):
    """增加时间按钮"""
    def __init__(self):
        super().__init__()

    def init_self(self):
        """初始化部件"""
        self.printer = QPixmap(".\\Icon\\DownArrow_del.png")

class ConfirmButton(BaseButton):
    """确定按钮"""
    def __init__(self):
        super().__init__()

    def init_size(self):
        self.setMaximumSize(100, 50)
        self.setMinimumSize(100, 50)

    def init_self(self):
        self.setText("确定")
        

    def init_background(self):
        self.setStyleSheet("""
                color: #5ba585;
                background-color: #e1e1de;
                border-radius: 10px;
                """)

class FinishButton(BaseButton):
    """完成按钮"""
    def __init__(self):
        super().__init__()

    def init_size(self):
        self.setMaximumSize(100, 50)
        self.setMinimumSize(100, 50)

    def init_self(self):
        self.setText("提前结束")

    def init_background(self):
        self.setStyleSheet("""
                color: #5ba585;
                background-color: #e1e1de;
                border-radius: 10px;
                            """)
        


if __name__ == '__main__':
    app  = QApplication([])
    window = QWidget()
    window.setWindowTitle("Button")

    layout = QVBoxLayout()  
    layout.addWidget(UpButton())
    layout.addWidget(DownButton())
    window.setLayout(layout)
    window.show()
    app.exec()