from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QFileDialog,QDialog
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QTimer
import sys

from Widgets.Button_Box import FinishButton
from Widgets.Show_Box import BaseLabel


class Countdown(QDialog):
    def __init__(self):
        super().__init__()
        self.init_window()
        self.init_data()
        self.init_widget()
        self.init_layer()
        self.init_connect()

    def init_data(self):
        self.hour = 0
        self.minute = 0
        self.second = 0
        self.passed_hour = 0
        self.passed_minute = 0
        self.passed_second = 0
    
    def init_window(self):
        # 全屏
        self.setGeometry(0, 0, 1920, 1080)
        # 模式
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setWindowTitle("专注一件事情")


    def init_widget(self):
        self.main_layout = QVBoxLayout(self)
        self.timer = QTimer(self)
        self.time_label = BaseLabel()
        self.time_label.setText("初始化中")
        self.finish_button = FinishButton()

    def init_layer(self):
        self.main_layout.addWidget(self.time_label,alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.finish_button, alignment=Qt.AlignCenter)
    def init_connect(self):
        self.finish_button.clicked.connect(self.finish_in_advance)

    def countdown(self,hour, minute, second):
        self.time_label.setText(f"{hour}小时{minute}分钟{second}秒")
        self.hour = hour
        self.minute = minute
        self.second = second
        self.timer.start(1000)
        self.timer.timeout.connect(self.update_time)
        
    def update_time(self):
        if self.second > 0:
            self.second -= 1
        elif self.minute > 0:
            self.minute -= 1
            self.second = 59
        elif self.hour > 0:
            self.hour -= 1
            self.minute = 59
            self.second = 59
        else:
            self.timer.finish()
        self.passed_second += 1
        if self.passed_second == 60:
            self.passed_minute += 1
            self.passed_second = 0
        if self.passed_minute == 60:
            self.passed_hour += 1
            self.passed_minute = 0
        self.time_label.setText(f"{self.hour}小时{self.minute}分钟{self.second}秒")

    def finish(self):
        # 完成，关闭窗口
        self.timer.stop()
        self.time_label.setText("时间到")
        self.finish_button.setText("时间到")

    def finish_in_advance(self):
        # 提前完成，关闭窗口
        self.close()



if __name__ == '__main__':

    app = QApplication(sys.argv)
    countdown = Countdown()
    countdown.exec()
    sys.exit(app.exec())