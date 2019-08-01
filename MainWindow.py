from PyQt5.QtWidgets import (QWidget, QApplication, QPushButton,
                             QVBoxLayout, QHBoxLayout, QMessageBox)
from PyQt5.QtGui import QPainter, QColor, QPalette, QPixmap
from PyQt5 import QtGui, QtWidgets, QtCore
import sys
import gesmuse_UI.hisworkWin as hisworkWin
import gesmuse_UI.helpWindow as helpWin
import gesmuse_UI.settingWin as settingWin
import gesmuse_UI.startWin as startWin
from gesmuse_UI.button_design import Button
import my_cv

import time
import drums
import Call


class Ges(QWidget):
    def __init__(self, eye, drum, a, s):
        super().__init__()
        self.eye = eye
        self.drum = drum
        self.a = a
        self.s = s
        self.initUI()

    def initUI(self):
        # 创建按钮
        startbutn = Button.StartButton(self)
        hisworkbutn = Button.OpusButton(self)
        settingbutn = Button.SettingButton(self)
        helpbutn = Button.HelpButton(self)
        quitbutn = Button.ExitButton(self)
        # 为按钮添加功能
        startbutn.clicked.connect(lambda: self.changeWindow(self.eye, self.drum, a, s))
        hisworkbutn.clicked.connect(self.hisworkWindow)
        settingbutn.clicked.connect(lambda: self.settingWindow(self.eye))  # 用lambda表达式实现参数传递！
        helpbutn.clicked.connect(self.helpWindow)
        quitbutn.clicked.connect(self.close)

        # 窗口布局
        hbox = QHBoxLayout()
        hbox.addStretch(5)
        hbox.addWidget(startbutn)
        hbox.addStretch(1)
        # hbox.addWidget(hisworkbutn)
        # hbox.addStretch(1)
        # 我的作品功能正在开发中
        hbox.addWidget(settingbutn)
        hbox.addStretch(1)
        hbox.addWidget(helpbutn)
        hbox.addStretch(1)
        hbox.addWidget(quitbutn)
        hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(4)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.setLayout(vbox)

        # self.setFixedSize(1152, 648)  # 固定窗口大小
        self.showFullScreen()  # 全屏
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        self.setWindowTitle("Gesmuse")
        self.show()

    # 设置背景图片
    def paintEvent(self, QPaintEvent):
        painter = QPainter(self)
        painter.drawRect(self.rect())
        pixmap = QPixmap(".//gesmuse_resources//image//MainBack.jpg")
        painter.drawPixmap(self.rect(), pixmap)

    # 跳转到创作页面
    def changeWindow(self, eye, drum, a, s):
        self.startWin = startWin.StartWindow()  # startwindow有些莫名其妙的错误，先用settingwindow代替
        self.startWin.show()
        BEAT_TIME = 0.5  # 给一个声音元素留的时间
        # eye.frame_show()
        begin = time.time()
        end = time.time()
        clock = 0
        while (1):
            end = time.time()
            clock += end - begin
            begin = end
            print('0')

            num = Call.run(eye.img_get(), a, s)
            key = eye.img_show()
            print(num)
            if clock > BEAT_TIME:
                drum.beat(num)
                clock = 0
            if key == 27:
                break

        eye.img_close()
        drum.store()

        self.startWin.exec_()

    # 跳转到历史作品页面
    def hisworkWindow(self):
        hisWin = hisworkWin.HisworkWindow()
        hisWin.show()
        hisWin.exec_()

    # 跳转到校准页面
    def settingWindow(self, eye):
        self.setWin = settingWin.SettingWindow()
        self.setWin.show()
        eye.frame_show()
        self.setWin.exec_()

    # 跳转到帮助页面
    def helpWindow(self):
        helWin = helpWin.HelpWindow()
        helWin.show()
        helWin.exec_()


if __name__ == '__main__':
    drum = drums.Drums('./sound1/')
    eye = my_cv.My_eye()
    a, s = Call.init()

    app = QApplication(sys.argv)
    ges = Ges(eye, drum, a, s)
    sys.exit(app.exec_())

    del eye
    del drum
