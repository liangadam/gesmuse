import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout


class Button(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()  # 界面绘制交给InitUi方法

    def initUI(self):
        # 控件QPushButton的定义和设置
        startButton = QPushButton(self)
        startButton.setMinimumSize(50, 100)  # 设置最小大小，主页面按钮图标原尺寸为200:400，为使图标不变形，请保持比例不变
        startButton.setStyleSheet("QPushButton{border-image: url(../gesmuse_resources/image/start_img-1.png)}"
                                  "QPushButton:hover{border-image: url(../gesmuse_resources/image/start_img-2.png)}"
                                  "QPushButton:pressed{border-image: url(../gesmuse_resources/image/start_img-1.png)}")
        opusButton = QPushButton(self)
        opusButton.setMinimumSize(50, 100)
        opusButton.setStyleSheet("QPushButton{border-image: url(../gesmuse_resources/image/opus_img-1.png)}"
                                 "QPushButton:hover{border-image: url(../gesmuse_resources/image/opus_img-2.png)}"
                                 "QPushButton:pressed{border-image: url(../gesmuse_resources/image/opus_img-1.png)}")

        settingButton = QPushButton()
        settingButton.setMinimumSize(50, 100)
        settingButton.setStyleSheet("QPushButton{border-image: url(../gesmuse_resources/image/setting_img-1.png)}"
                                    "QPushButton:hover{border-image: url(../gesmuse_resources/image/setting_img-2.png)}"
                                    "QPushButton:pressed{border-image: url(../gesmuse_resources/image/setting_img-1.png)}")

        helpButton = QPushButton()
        helpButton.setMinimumSize(50, 100)
        helpButton.setStyleSheet("QPushButton{border-image: url(../gesmuse_resources/image/help_img-1.png)}"
                                 "QPushButton:hover{border-image: url(../gesmuse_resources/image/help_img-2.png)}"
                                 "QPushButton:pressed{border-image: url(../gesmuse_resources/image/help_img-1.png)}")

        exitButton = QPushButton()
        exitButton.setMinimumSize(50, 100)
        exitButton.setStyleSheet("QPushButton{border-image: url(../gesmuse_resources/image/exit_img-1.png)}"
                                 "QPushButton:hover{border-image: url(../gesmuse_resources/image/exit_img-2.png)}"
                                 "QPushButton:pressed{border-image: url(../gesmuse_resources/image/exit_img-1.png)}")

        # 布局
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(startButton)
        hbox.addWidget(opusButton)
        hbox.addWidget(settingButton)
        hbox.addWidget(helpButton)
        hbox.addWidget(exitButton)
        hbox.addStretch(1)

        # 设置布局
        self.setLayout(hbox)
        # 设置窗口的位置和大小
        self.setGeometry(300, 300, 1000, 800)
        # 设置窗口的标题
        self.setWindowTitle('Gesmuse_Button')
        self.show()


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    ex = Button()
    sys.exit(app.exec_())
