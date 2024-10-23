from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget, QPushButton, QSpinBox,QHBoxLayout
from PySide6.QtCore import QTimer, QTime, Qt,QDate
from PySide6.QtGui import QIcon, QFont

class BaseLabel(QLabel):
    """基础标签"""
    def __init__(self):
        super().__init__()
        self.init_widget()

    def init_widget(self):
        """初始化部件"""
        self.setFont(QFont("Arial", 40))
        self.setAlignment(Qt.AlignCenter)


class WelcomeLabel(BaseLabel):
    """欢迎语"""
    def __init__(self):
        super().__init__()
        self.init_timer()

    def init_widget(self):
        """初始化部件"""
        self.update_time()
        self.setFont(QFont("Arial", 40))
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("""
            color: red;
            background-color: yellow;
            """)
    def init_timer(self):
        """初始化定时器"""
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

    def update_time(self):
        """更新时间"""
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        self.setText(f"欢迎使用倒计时，\n今天是{current_date.toString('yyyy年MM月dd日')}，\n当前时间是{current_time.toString('hh:mm:ss')}")


class NumLabel(BaseLabel):
    """数字标签,分钟和秒的显示"""
    def __init__(self,num):
        super().__init__()
        self.setText(str(num))

    def init_widget(self):
        """初始化部件"""
        self.setFont(QFont("Arial", 40))
        self.setAlignment(Qt.AlignCenter)
    
    def up_num(self):
        """数字加一"""
        num = int(self.text())
        if num < 60:
            self.setText(str(num+1))
        else:
            self.setText("1")

    def down_num(self):
        """数字减一"""
        num = int(self.text())
        if num > 0:
            self.setText(str(num-1))
        else:
            self.setText("59")


class HourLabel(NumLabel):
    """小时的显示"""
    def up_num(self):
        """数字加一"""
        num = int(self.text())
        if num < 24:
            self.setText(str(num+1))
        else:
            self.setText("1")

    def down_num(self):
        """数字减一"""
        num = int(self.text())
        if num > 0:
            self.setText(str(num-1))
        else:
            self.setText("23")

class EndLabel(BaseLabel):
    """倒计时结束的标签"""
    def __init__(self):
        super().__init__()
