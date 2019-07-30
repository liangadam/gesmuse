#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' my_cv '

__author__ = 'Adam'

import numpy as np
import cv2

# 标记检测区域向下偏移量
PD = 60
zero = np.zeros((256, 256, 3), np.int32)


class My_eye(object):
    # 构造函数：px,py为窗口位置，raw,col为检测区域的大小
    def __init__(self, px=217, py=377, raw=256, col=256):
        self.px = px
        self.py = py
        self.raw = raw
        self.col = col
        self.img = np.zeros((raw, col), np.uint8)  # 二维0/1矩阵，传给神经网络
        self.frame = np.zeros((480, 640, 3))
        self.cap = cv2.VideoCapture(0)  # 打开摄像头

    # 程序结束后记得用del清除实例,关闭摄像头
    def __del__(self):
        self.cap.release()

    # 校准页使用，让用户了解手的位置
    def frame_show(self):
        cv2.namedWindow('frame')
        cv2.moveWindow('frame', self.py, self.px)

        while (1):
            ret, self.frame = self.cap.read()
            frame2 = self.frame.copy()
            cv2.rectangle(frame2, (0, PD), (self.raw - 1, self.col + PD - 1), (255, 255, 255), 3)
            cv2.imshow('frame', frame2)
            k = cv2.waitKey(5) & 0xff
            if k == 27:
                print('succeed!')
                break
        cv2.destroyAllWindows()

    # x与y坐标位置相反(但画长方形时没有反)
    # 音乐创作页使用，让用户实时看到自己手的位形
    def voi_show(self):
        voi2 = self.frame[PD:self.col + PD, 0:self.raw].copy().astype(np.int32)
        cv2.namedWindow('voi')
        cv2.moveWindow('voi', self.py, self.px)
        while (1):
            ret, self.frame = self.cap.read()
            voi = self.frame[PD:self.col + PD, 0:self.raw].astype(np.int32)
            # 做差
            sub = np.abs(voi - voi2).astype(np.uint8)
            # 灰度化
            sub_gray = cv2.cvtColor(sub, cv2.COLOR_BGR2GRAY)
            # 二值化
            ret1, img = cv2.threshold(sub_gray, 20, 80, cv2.THRESH_BINARY)  # ???

            kernel = np.ones((5, 5), np.uint8)
            opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
            closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
            # ct1=cv2.morphologyEx(closing, cv2.MORPH_GRADIENT, kernel)
            ct2 = cv2.Canny(closing, 100, 200)  # ???
            ct3, hierarchy = cv2.findContours(ct2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            # 新建图层
            img2 = np.zeros((self.raw, self.col), np.uint8)
            # 挑选主体图层

            # cv2.imwrite('hand_result.jpg',img2)
            # print(len(ct3))
            l = ([len(ct3[i]) for i in range(len(ct3))])
            if l:
                n = l.index(max(l))
                cv2.drawContours(img2, ct3, n, 255, 2)
                self.img = sub_gray
            # print(n)

            cv2.imshow('voi', img2)
            k = cv2.waitKey(1) & 0xff
            if k == ord('w'):
                cv2.imwrite('test.jpg', img)
            elif k == 27:
                break
        cv2.destroyAllWindows()
