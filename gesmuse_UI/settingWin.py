from PyQt5.QtWidgets import QDesktopWidget,QDialog,QPushButton


class SettingWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.initSW()

    def initSW(self):
        quitbutn_sw=QPushButton("返回")

        self.setFixedSize(1152, 648)
        self.setWindowTitle('设置')
        self.center()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)