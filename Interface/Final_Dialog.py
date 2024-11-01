from PySide6.QtWidgets import QDialog,QWidget,QLabel,QVBoxLayout,QHBoxLayout,QPushButton,QMessageBox,QLineEdit
from PySide6.QtCore import Qt,QTimer
from PySide6.QtGui import QFont

from Widgets.Show_Box import EndLabel

class Final_Dialog(QDialog):
    def __init__(self,passed_time):
        super().__init__()
        self.init_window()
        self.init_widget()
        self.init_layer()
        self.init_connect()
        self.init_time(passed_time)

    def init_window(self):
        self.setWindowTitle("倒计时结束")
        self.setFixedSize(1000,700)

    def init_widget(self):
        self.Vlayout = QVBoxLayout(self)
        self.show_label = EndLabel()
    
    def init_layer(self):
        self.Vlayout.addWidget(self.show_label)

    def init_connect(self):
        pass


    def init_time(self,passed_time):
        self.passed_time = {}
        self.passed_time['hour'] = passed_time[0]
        self.passed_time['minute'] = passed_time[1]
        self.passed_time['second'] = passed_time[2]
        self.time_str = f"本次专注时间为：{self.passed_time['hour']}小时{self.passed_time['minute']}分钟{self.passed_time['second']}秒"
        self.show_label.setText(self.time_str)

    def __str__(self) -> str:
        return self.time_str
    