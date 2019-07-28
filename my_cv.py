#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' my_cv '

__author__ = 'Adam'

import numpy as np
import cv2

#标记检测区域向下偏移量
PD=0


class My_eye(object):
    #构造函数：px,py为窗口位置，raw,col为检测区域的大小
    def __init__(self,px=200,py=200,raw=256,col=256):
        self.px=px
        self.py=py
        self.raw=raw
        self.col=col
        self.img=np.zeros((raw,col),np.uint8)#二维0/1矩阵，传给神经网络
        self.frame=np.zeros((480,640,3))
        self.cap=cv2.VideoCapture(0)#打开摄像头
        
    #程序结束后记得用del清除实例,关闭摄像头
    def __del__(self):
        self.cap.release()
        
    #校准页使用，让用户了解手的位置
    def frame_show(self):
        cv2.namedWindow('frame')
        cv2.moveWindow('frame',self.py,self.px)
        
        while(1):
            ret,self.frame=self.cap.read()
            
            cv2.rectangle(self.frame,(0,PD),(self.raw-1,self.col+PD-1),(255,255,255),3)
            cv2.imshow('frame',self.frame)
            k=cv2.waitKey(5)&0xff
            if k==27:
                print('succeed!')
                break
        cv2.destroyAllWindows()
        
    #x与y坐标位置相反(但画长方形时没有反)
    #音乐创作页使用，让用户实时看到自己手的位形
    def voi_show(self):
        voi=self.frame[PD:self.col+PD-1,0:self.raw-1].copy()
        #取反
        voi_not=cv2.bitwise_not(voi)
        cv2.namedWindow('voi')
        cv2.moveWindow('voi',self.py,self.px)
        while(1):
            ret,self.frame=self.cap.read()
            voi=self.frame[PD:self.col+PD-1,0:self.raw-1]
            #做差
            sub=cv2.bitwise_and(voi_not,voi)
            #灰度化
            sub_gray=cv2.cvtColor(sub,cv2.COLOR_BGR2GRAY)
            #二值化
            ret1,img=cv2.threshold(sub_gray,30,100,cv2.THRESH_BINARY)#???

            kernel = np.ones((5,5),np.uint8)
            opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
            closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
            #ct1=cv2.morphologyEx(closing, cv2.MORPH_GRADIENT, kernel)
            ct2=cv2.Canny(closing,100,200)#???
            ct3, hierarchy = cv2.findContours(ct2,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

            #新建图层
            img2=np.zeros((self.raw,self.col),np.uint8)
            #挑选主体图层

            #cv2.imwrite('hand_result.jpg',img2)
            #print(len(ct3))
            l=([len(ct3[i]) for i in range(len(ct3))])
            if l:
                n=l.index(max(l))
                cv2.drawContours(img2,ct3,n,255,2)
                self.img=img2/255
            #print(n)
            
            cv2.imshow('voi',img2)
            k=cv2.waitKey(1)&0xff
            if k==ord('w'):
                cv2.imwrite('test.jpg',img)
            elif k==27:
                break
        print(img2.shape)
        cv2.destroyAllWindows()
