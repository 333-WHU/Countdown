from PySide6.QtWidgets import QWidget,QDialog
from PySide6.QtGui import QIcon
from abc import abstractmethod


class BaseWidget(QWidget):
    """基础部件，作为窗口的基础部件,必须实现2，3，4。\n
    1 初始化窗口\n
    2 初始化控件\n
    3 初始化布局\n
    4 连接信号和槽"""
    def __init__(self):
        super().__init__()
        self.init_window()
        self.init_widget()
        self.init_layer()
        self.init_connect()

    def init_window(self):
        '''初始化窗口'''
        self.setWindowIcon(QIcon(".\\sourse\\首页图标.jpg"))# 设置窗口图标
        self.setWindowTitle("专注时间")# 设置窗口标题
        self.setGeometry(400, 200, 600, 400)# 设置窗口大小

    @abstractmethod
    def init_widget(self):
        '''初始化控件'''
        
    @abstractmethod
    def init_layer(self):
        '''初始化布局'''
        

    @abstractmethod
    def init_connect(self):
        '''连接信号和槽'''

class BaseDialog(QDialog):
    """基础对话框，作为窗口的基础部件,必须实现2，3，4\n
    1 初始化窗口\n
    2 初始化控件\n
    3 初始化布局\n
    4 连接信号和槽\n"""
    def __init__(self):
        super().__init__()
        self.init_window()
        self.init_widget()
        self.init_layer()
        self.init_connect()

    def init_window(self):
        '''初始化窗口'''
        self.setWindowIcon(QIcon(".\\sourse\\首页图标.jpg"))# 设置窗口图标
        self.setWindowTitle("专注时间")
        self.setGeometry(400, 200, 600, 400)# 设置窗口大小

    @abstractmethod
    def init_widget(self):
        '''初始化控件'''

    @abstractmethod
    def init_layer(self):
        '''初始化布局'''

    @abstractmethod
    def init_connect(self):
        '''连接信号和槽'''
