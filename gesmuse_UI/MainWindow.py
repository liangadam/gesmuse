from PyQt5.QtWidgets import (QWidget, QApplication, QPushButton,
                             QVBoxLayout, QHBoxLayout)
from PyQt5.QtGui import QPainter, QColor, QPalette, QPixmap
from PyQt5 import QtGui, QtWidgets, QtCore
import sys
import gesmuse_UI.hisworkWin as hisworkWin
import gesmuse_UI.helpWindow as helpWin
import  gesmuse_UI.settingWin as settingWin


class Ges(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建按钮
        startbutn = QPushButton('开\n始\n创\n作')
        hisworkbutn = QPushButton('我\n的\n作\n品')
        settingbutn = QPushButton('设\n\n\n置')
        helpbutn = QPushButton('教\n\n\n程')
        quitbutn = QPushButton('退\n\n\n出')
        # 为按钮添加功能
        startbutn.clicked.connect(self.changeWindow)
        hisworkbutn.clicked.connect(self.hisworkWindow)
        settingbutn.clicked.connect(self.settingWindow)
        helpbutn.clicked.connect(self.helpWindow)
        quitbutn.clicked.connect(self.close)
        # 设置按钮外观
        startbutn.setFixedSize(50, 200)
        hisworkbutn.setFixedSize(50, 200)
        settingbutn.setFixedSize(50, 200)
        helpbutn.setFixedSize(50, 200)
        quitbutn.setFixedSize(50, 200)

        myfont = QtGui.QFont('楷体', 18)
        myfont.setBold(True)
        startbutn.setFont(myfont)
        hisworkbutn.setFont(myfont)
        settingbutn.setFont(myfont)
        helpbutn.setFont(myfont)
        quitbutn.setFont(myfont)

        """
        设置按钮背景图
        quitbutn.setStyleSheet("QPushButton{border-image: url(butn3.png)}")
        
        按钮透明
        op = QtWidgets.QGraphicsOpacityEffect()
        op.setOpacity(0)
        quitbutn.setGraphicsEffect(op)
        """
        # 窗口布局
        hbox = QHBoxLayout()
        hbox.addStretch(5)
        hbox.addWidget(startbutn)
        hbox.addStretch(1)
        hbox.addWidget(hisworkbutn)
        hbox.addStretch(1)
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

        #self.setFixedSize(1152, 648)  # 固定窗口大小
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        self.setWindowTitle("Gesmuse")
        self.show()

    # 设置背景图片
    def paintEvent(self, QPaintEvent):
        painter = QPainter(self)
        painter.drawRect(self.rect())
        pixmap = QPixmap("..//gesmuse_resources//picture//MainBack.jpg")
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
        setWin=settingWin.SettingWindow()
        setWin.show()
        setWin.exec_()

    def helpWindow(self):
        helWin=helpWin.HelpWindow()
        helWin.show()
        helWin.exec_()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ges = Ges()
    ges.showFullScreen()
    sys.exit(app.exec_())
