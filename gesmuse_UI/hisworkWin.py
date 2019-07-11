from PyQt5.QtWidgets import (QDesktopWidget, QDialog, QPushButton,
                             QVBoxLayout, QHBoxLayout, QLabel)
from PyQt5 import QtGui


class HisworkWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.initHW()

    def initHW(self):
        title = QLabel("帮助文档")
        titlefont = QtGui.QFont('楷体', 24)
        titlefont.setBold(True)
        title.setFont(titlefont)

        quitbutn_hw = QPushButton("返回")
        quitbutn_hw.clicked.connect(self.close)

        titlehbox=QHBoxLayout()
        titlehbox.addWidget(title)

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
