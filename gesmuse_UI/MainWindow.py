from PyQt5.QtWidgets import (QWidget, QApplication, QPushButton,
                             QVBoxLayout, QHBoxLayout)
from PyQt5.QtGui import QPainter, QColor, QPalette, QPixmap
from PyQt5 import QtGui, QtWidgets, QtCore
import sys
import gesmuse_UI.hisworkWin as hisworkWin
import gesmuse_UI.helpWindow as helpWin
import gesmuse_UI.settingWin as settingWin
from gesmuse_UI.button_design import Button
import my_cv


class Ges(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建按钮
        startbutn = Button.StartButton(self)
        hisworkbutn = Button.OpusButton(self)
        settingbutn = Button.SettingButton(self)
        helpbutn = Button.HelpButton(self)
        quitbutn = Button.ExitButton(self)
        # 为按钮添加功能
        startbutn.clicked.connect(self.changeWindow)
        hisworkbutn.clicked.connect(self.hisworkWindow)
        settingbutn.clicked.connect(self.settingWindow)
        helpbutn.clicked.connect(self.helpWindow)
        quitbutn.clicked.connect(self.close)
        # 设置按钮外观

        # 窗口布局
        hbox = QHBoxLayout()
        hbox.addStretch(5)
        hbox.addWidget(startbutn)
        hbox.addStretch(1)
        # hbox.addWidget(hisworkbutn)
        # hbox.addStretch(1)
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
        self.showFullScreen()
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        self.setWindowTitle("Gesmuse")
        self.show()

    # 设置背景图片
    def paintEvent(self, QPaintEvent):
        painter = QPainter(self)
        painter.drawRect(self.rect())
        pixmap = QPixmap("..//gesmuse_resources//image//MainBack.jpg")
        painter.drawPixmap(self.rect(), pixmap)

    # 跳转到创作页面
    def changeWindow(self):
        pass

    # 跳转到历史作品页面
    def hisworkWindow(self):
        hisWin = hisworkWin.HisworkWindow()
        hisWin.show()
        hisWin.exec_()

    def settingWindow(self):
        self.setWin = settingWin.SettingWindow()
        self.setWin.show()
        eye = my_cv.My_eye()
        eye.frame_show()
        self.setWin.exec_()


    def helpWindow(self):
        helWin = helpWin.HelpWindow()
        helWin.show()
        helWin.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ges = Ges()
    sys.exit(app.exec_())
