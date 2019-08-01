from PyQt5.QtWidgets import (QDesktopWidget, QDialog, QPushButton,
                             QHBoxLayout, QVBoxLayout, QCheckBox, QLabel)
from PyQt5.QtCore import Qt,pyqtSignal
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QPainter,QPixmap
from gesmuse_UI.button_design import Button


class SettingWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.initSW()

    def initSW(self):
        cbfont = QtGui.QFont('楷体', 18)
        cbfont.setBold(True)

        reminderlabel=QLabel("校准时尽量调整电脑使白色方框内视野为白色墙壁")
        helplabel=QLabel("完成校准后连按ESC键两次即可快速退出")
        reminderlabel.setFont(cbfont)
        helplabel.setFont(cbfont)

        quitbutn_sw = Button.BackButton(self)
        quitbutn_sw.clicked.connect(self.close)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(reminderlabel)
        vbox.addWidget(helplabel)

        self.setLayout(vbox)

        self.setFixedSize(641, 550)
        self.setWindowTitle('设置')
        self.center()



    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)



    def paintEvent(self, QPaintEvent):
        painter = QPainter(self)
        painter.setBrush(Qt.white)
        painter.drawRect(self.rect())
        #pixmap = QPixmap(".//gesmuse_resources//image//chidback.jpg")
        #painter.drawPixmap(self.rect(), pixmap)
