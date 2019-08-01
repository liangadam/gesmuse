
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton,QDialog
from PyQt5.QtWidgets import QMessageBox, QAction, QToolTip,QLabel
from PyQt5.QtGui import QFont,QPalette, QBrush, QPixmap
from PyQt5.QtWidgets import QHBoxLayout, qApp, QVBoxLayout
from PyQt5.QtCore import QCoreApplication
from PyQt5 import QtCore
import pygame

class StartWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.init_stw()

    def init_stw(self):
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


    def paintEvent(self, QPaintEvent):
        painter = QPainter(self)
        painter.setBrush(Qt.black)
        painter.drawRect(self.rect())
      

