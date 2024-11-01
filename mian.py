from PySide6.QtWidgets import QApplication
from Interface.Countdown_index import CountdownIndex
from Interface.Countdown_main import Countdown
from Interface.Final_Dialog import Final_Dialog


class MainFramework():
    def __init__(self):
        self.init_widget()
        self.init_data()
        self.init_connect()

    def init_data(self):
        '''初始化数据'''
        self.index_clicked = False

    def init_widget(self):
        '''初始化首页'''
        self.countdown_index = CountdownIndex()

    def init_connect(self):
        '''初始化信号槽'''
        self.countdown_index.confirm_button.clicked.connect(self.show_main)

    def start_countdown(self):
        '''开始倒计时'''
        hour = int(str(self.countdown_index.down_widget.hour_count))
        minute = int(str(self.countdown_index.down_widget.minute_count))
        second = int(str(self.countdown_index.down_widget.second_count))
        self.countdown_main.countdown(hour, minute, second)

    def show_index(self):
        '''显示首页'''
        self.countdown_index.show()

    def show_main(self):
        '''显示主界面'''
        if not self.index_clicked:
            self.countdown_main = Countdown()
            self.countdown_main.finish_button.clicked.connect(self.show_final)
            self.countdown_main.finish_button.clicked.connect(self.show_final)
            self.index_clicked = True
        self.start_countdown()
        self.countdown_main.show()
        self.countdown_index.close()
        

    def show_final(self):
        '''显示最终界面'''
        passed_hour = self.countdown_main.passed_hour
        passed_minute = self.countdown_main.passed_minute
        passed_second = self.countdown_main.passed_second
        self.final_dialog = Final_Dialog([passed_hour,passed_minute,passed_second])
        self.final_dialog.show()




if __name__ == '__main__':
    app = QApplication([])
    main_frame = MainFramework()
    main_frame.show_index()
    app.exec()