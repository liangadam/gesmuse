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

        quitbutn_sw = Button.BackButton(self)
        quitbutn_sw.clicked.connect(self.close)

        quithbox=QHBoxLayout()
        quithbox.addStretch(1)
        quithbox.addWidget(quitbutn_sw)

        vbox = QVBoxLayout()

        vbox.addStretch(1)
        vbox.addLayout(quithbox)

        self.setLayout(vbox)

        self.setFixedSize(1152, 648)
        self.setWindowTitle('设置')
        self.center()



    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

    def calibration(self):
        pass


    def paintEvent(self, QPaintEvent):
        painter = QPainter(self)
        painter.setBrush(Qt.black)
        painter.drawRect(self.rect())
        # pixmap = QPixmap("..//gesmuse_resources//image//chidback.jpg")
        # painter.drawPixmap(self.rect(), pixmap)