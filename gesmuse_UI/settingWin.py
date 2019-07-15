from PyQt5.QtWidgets import (QDesktopWidget, QDialog, QPushButton,
                             QHBoxLayout, QVBoxLayout, QCheckBox, QLabel)
from PyQt5.QtCore import Qt,pyqtSignal
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QPainter,QPixmap

class SettingWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.initSW()

    def initSW(self):
        cb = QCheckBox("全屏", self)
        cb.setChecked(True)
        cbfont = QtGui.QFont('楷体', 24)
        cbfont.setBold(True)
        cb.setFont(cbfont)

        calibrationbtn = QPushButton("校准")
        calibrationbtn.setFont(cbfont)
        calibrationbtn.clicked.connect(self.calibration)

        quitbutn_sw = QPushButton("返回")
        quitbutn_sw.setFont(cbfont)
        quitbutn_sw.clicked.connect(self.close)

        vbox = QVBoxLayout()
        vbox.addWidget(cb)
        vbox.addWidget(calibrationbtn)
        vbox.addStretch(1)
        vbox.addWidget(quitbutn_sw)

        self.setLayout(vbox)

        self.setFixedSize(576, 648)
        self.setWindowTitle('设置')
        self.center()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

    def calibration(self):
        pass

    my_signal = pyqtSignal(str)

    def closeEvent(self, event):
        content = self.cb.isChecked()
        self.my_signal.emit(content)

    def paintEvent(self, QPaintEvent):
        painter = QPainter(self)
        painter.drawRect(self.rect())
        pixmap = QPixmap("..//gesmuse_resources//image//chidback.jpg")
        painter.drawPixmap(self.rect(), pixmap)