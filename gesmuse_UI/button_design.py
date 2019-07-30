"""
调用示例：
from gesmuse_UI.button_design import Button
startbutton = Button.StartButton(self)
"""

from PyQt5.QtWidgets import QPushButton


class Button:

    def __init__(self):
        pass

    def StartButton(self):
        startButton = QPushButton()
        startButton.setMinimumSize(100, 200)  # 设置最小大小，主页面按钮图标原尺寸为200:400，为使图标不变形，请保持比例不变
        startButton.setStyleSheet("QPushButton{border-image: url(../gesmuse_resources/image/start_img-1.png)}"
                                  "QPushButton:hover{border-image: url(../gesmuse_resources/image/start_img-2.png)}"
                                  "QPushButton:pressed{border-image: url(../gesmuse_resources/image/start_img-1.png)}")
        return startButton

    def OpusButton(self):
        opusButton = QPushButton()
        opusButton.setMinimumSize(100, 200)
        opusButton.setStyleSheet("QPushButton{border-image: url(../gesmuse_resources/image/opus_img-1.png)}"
                                 "QPushButton:hover{border-image: url(../gesmuse_resources/image/opus_img-2.png)}"
                                 "QPushButton:pressed{border-image: url(../gesmuse_resources/image/opus_img-1.png)}")
        return opusButton

    def SettingButton(self):
        settingButton = QPushButton()
        settingButton.setMinimumSize(100, 200)
        settingButton.setStyleSheet("QPushButton{border-image: url(../gesmuse_resources/image/setting_img-1.png)}"
                                    "QPushButton:hover{border-image: url(../gesmuse_resources/image/setting_img-2.png)}"
                                    "QPushButton:pressed{border-image: url(../gesmuse_resources/image/setting_img-1.png)}")
        return settingButton

    def HelpButton(self):
        helpButton = QPushButton()
        helpButton.setMinimumSize(100, 200)
        helpButton.setStyleSheet("QPushButton{border-image: url(../gesmuse_resources/image/help_img-1.png)}"
                                 "QPushButton:hover{border-image: url(../gesmuse_resources/image/help_img-2.png)}"
                                 "QPushButton:pressed{border-image: url(../gesmuse_resources/image/help_img-1.png)}")
        return helpButton

    def ExitButton(self):
        exitButton = QPushButton()
        exitButton.setMinimumSize(100, 200)
        exitButton.setStyleSheet("QPushButton{border-image: url(../gesmuse_resources/image/exit_img-1.png)}"
                                 "QPushButton:hover{border-image: url(../gesmuse_resources/image/exit_img-2.png)}"
                                 "QPushButton:pressed{border-image: url(../gesmuse_resources/image/exit_img-1.png)}")
        return exitButton

    def BackButton(self):
        backButton = QPushButton()
        backButton.setMinimumSize(100, 200)
        backButton.setStyleSheet("QPushButton{border-image: url(../gesmuse_resources/image/back_img-1.png)}"
                                 "QPushButton:hover{border-image: url(../gesmuse_resources/image/back_img-2.png)}"
                                 "QPushButton:pressed{border-image: url(../gesmuse_resources/image/back_img-1.png)}")
        return backButton