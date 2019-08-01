from PyQt5.QtWidgets import (QDesktopWidget, QDialog, QPushButton,
                             QVBoxLayout, QHBoxLayout, QLabel,QScrollArea)
from PyQt5 import QtGui,QtCore
from PyQt5.QtGui import QPainter, QPixmap,QFont,QPalette,QColor

text="""
step1：
    点击设置按钮，打开校准页面，您会注意到您的摄像头已被调用，画面中使用白色
矩形框起的区域就是您的手势感知区域，此过程软件将获取白色框内的背景，因此请您
不要将身体的任何部位放入白色矩形框中，按下ESC键退出此页面。
    请注意：为保证校准效果，在完成校准后，请不要再移动您的摄像头，并且尽可能
保持摄像设备的稳定。
step2:
    点击开始创作按钮，进入创作页面，手势识别启动，这时您可以将您的右手放入白
色矩形框，开始您的音乐创作。

声明:
    此版本为gesmuse初代产品，在今后的产品中，你们可以更轻松的创造更多自己作
词、作曲、编舞（手指舞）的原创作品，期待的话，就多多支持吧！
"""

class HelpWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.initHPW()

    def initHPW(self):
        #设置标题
        title = QLabel("帮助文档")
        #title.setStyleSheet("color:white")
        titlefont = QtGui.QFont('楷体', 24)
        titlefont.setBold(True)
        title.setFont(titlefont)
        #设置返回按钮
        quitbutn_hpw = QPushButton("返回")
        quitbutn_hpw.clicked.connect(self.close)
        #文本
        self.tlabel=QLabel()
        self.tlabel.setText(text)
        self.tlabel.setFont(QFont("宋体", 16))
        #self.setStyleSheet("QLabel{background:white;}")
        #
        myscroll=QScrollArea()
        myscroll.setWidget(self.tlabel)
        myscroll.resize(830,400)
        #设置布局
        titlehbox = QHBoxLayout()
        titlehbox.addStretch(1)
        titlehbox.addWidget(title)
        titlehbox.addStretch(1)

        labelhbox=QHBoxLayout()
        labelhbox.addWidget(myscroll)


        endhbox = QHBoxLayout()
        endhbox.addStretch(1)
        endhbox.addWidget(quitbutn_hpw)

        vbox = QVBoxLayout()
        vbox.addLayout(titlehbox)
        vbox.addLayout(labelhbox)
        vbox.addLayout(endhbox)

        self.setLayout(vbox)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setFixedSize(830, 600)
        self.setWindowTitle('教程')
        self.center()


    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)


    def paintEvent(self, QPaintEvent):
        painter = QPainter(self)
        #painter.setBrush(Qt.black)
        painter.drawRect(self.rect())
        pixmap = QPixmap(".//gesmuse_resources//image//chidback.jpg")
        painter.drawPixmap(self.rect(), pixmap)
