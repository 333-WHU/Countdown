from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget, QPushButton, QSpinBox,QHBoxLayout
from PySide6.QtCore import QTimer, QTime, Qt,QDate
from PySide6.QtGui import QIcon, QFont

from Show_Box import WelcomeLabel,NumLabel,HourLabel
from Button_Box import UpButton,DownButton,ConfirmButton

class UpWidget(QWidget):
    """上方的部件，用来显示欢迎语"""
    def __init__(self):
        super().__init__()
        self.init_widget()
    
    def init_widget(self):
        """初始化部件"""
        self.midlayer = QVBoxLayout()
        self.setLayout(self.midlayer)
        self.welcome_label = WelcomeLabel()
        self.midlayer.addWidget(self.welcome_label)



class CountdownWidget(QWidget):
    """显示和按钮集合"""
    def __init__(self,b_hour=False):
        super().__init__()
        self.init_widget(b_hour)
        self.init_connect()
        self.init_layer()

    def init_widget(self,b_hour):
        """初始化部件"""
        self.midlayer = QVBoxLayout()
        self.setLayout(self.midlayer)

        self.up_button = UpButton()
        self.down_button = DownButton()
        if b_hour:
            self.show_label = HourLabel("0")
        else:
            self.show_label = NumLabel("0")

    def init_connect(self):
        """连接信号和槽"""
        self.up_button.clicked.connect(self.show_label.up_num)
        self.down_button.clicked.connect(self.show_label.down_num)

    def init_layer(self):
        self.midlayer.addWidget(self.up_button)
        self.midlayer.addWidget(self.show_label)
        self.midlayer.addWidget(self.down_button)
        # self.midlayer.addWidget(self.up_button,alignment=Qt.AlignCenter)
        # self.midlayer.addWidget(self.show_label,alignment=Qt.AlignCenter)
        # self.midlayer.addWidget(self.down_button,alignment=Qt.AlignCenter)
    
    def out_put(self):
        """输出数字"""
        return self.show_label.text()
    
    def __str__(self) -> str:
        return self.show_label.text()

class DownWidget(QWidget):
    """下方的部件，用来显示倒计时"""
    def __init__(self):
        super().__init__()
        self.init_widget()

    def init_widget(self):
        """初始化部件"""
        self.midlayer = QHBoxLayout()
        self.setLayout(self.midlayer)
        self.hour_count = CountdownWidget(True)
        self.midlayer.addWidget(self.hour_count)
        self.minute_count = CountdownWidget()
        self.midlayer.addWidget(self.minute_count)
        self.second_count = CountdownWidget()
        self.midlayer.addWidget(self.second_count)




        

class CountdownIndex(QWidget):
    def __init__(self):
        super().__init__()
        self.init_window()
        self.init_widget()
        self.init_layer()
        self.init_connect()

    
    def init_window(self):
        '''初始化窗口'''
        self.setWindowIcon(QIcon(".\\sourse\\首页图标.jpg!con"))# 设置窗口图标
        self.setWindowTitle("专注时间")# 设置窗口标题
        self.setGeometry(400, 200, 600, 400)# 设置窗口大小

    def init_widget(self):
        '''初始化控件'''
        self.up_widget = UpWidget()
        self.down_widget = DownWidget()
        self.confirm_button = ConfirmButton()


    def init_layer(self):
        '''初始化布局'''
        # 垂直布局
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        self.main_layout.addWidget(self.up_widget)
        self.main_layout.addWidget(self.down_widget)
        self.main_layout.addWidget(self.confirm_button,alignment=Qt.AlignCenter)

    def init_connect(self):
        '''连接信号和槽'''
        self.confirm_button.clicked.connect(self.confirm)
    
    def confirm(self):
        '''确定按钮的槽函数'''
        hour = int(self.down_widget.hour_count.out_put())
        minute = int(self.down_widget.minute_count.out_put())
        second = int(self.down_widget.second_count.out_put())
        output_str = f"{hour}小时{minute}分钟{second}秒"
        print(output_str)




if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication
    app = QApplication(sys.argv)
    window = CountdownIndex()
    window.show()
    sys.exit(app.exec())
