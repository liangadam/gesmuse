from PyQt5.QtWidgets import (QDesktopWidget, QDialog, QPushButton,
                             QVBoxLayout, QHBoxLayout, QLabel)
from PyQt5 import QtGui
from PyQt5.QtGui import QPainter,QPixmap


class HisworkWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.initHW()

    def initHW(self):
        title = QLabel("作品列表")
        titlefont = QtGui.QFont('楷体', 24)
        titlefont.setBold(True)
        title.setFont(titlefont)

        quitbutn_hw = QPushButton("返回")
        quitbutn_hw.clicked.connect(self.close)

        titlehbox=QHBoxLayout()
        titlehbox.addStretch(1)
        titlehbox.addWidget(title)
        titlehbox.addStretch(1)

        endhbox=QHBoxLayout()
        endhbox.addStretch(1)
        endhbox.addWidget(quitbutn_hw)

        vbox=QVBoxLayout()
        vbox.addLayout(titlehbox)
        vbox.addStretch(1)
        vbox.addLayout(endhbox)

        self.setLayout(vbox)

        self.setFixedSize(1152, 648)
        self.setWindowTitle('作品列表')
        self.center()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

    def paintEvent(self, QPaintEvent):
        painter = QPainter(self)
        painter.drawRect(self.rect())
        pixmap = QPixmap(".//gesmuse_resources//image//chidback.jpg")
        painter.drawPixmap(self.rect(), pixmap)
