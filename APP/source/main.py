#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' main '

__author__ = 'Adam'


BEAT_TIME=0.5#给一个声音元素留的时间
import Call
import my_cv
import drums
#import cv2
import time
#将几个界面的切换写到一个main里
if __name__ =='__main__':
    #这些是变量的初始化和对象创建，可考虑在进入界面就执行
    begin=time.time()
    end=time.time()
    clock=0
    drum=drums.Drums('./sound1/')
    eye=my_cv.My_eye()
    a,s=Call.init()
    
    #这个在校准界面使用，用户按esc后背景会被存入eye
    eye.frame_show()
    #JUMP
    #这个在创作界面使用，会在之前窗口同样坐标处生成手的窗口并播放声音，按esc退出
    while(1):
        end=time.time()
        clock+=end-begin
        begin=end
        num=Call.run(eye.img_get(),a,s)
        key=eye.img_show()
        print(num)
        if clock>BEAT_TIME:
            drum.beat(num)
            clock=0
        if key==27:
            break
    eye.img_close()
    drum.store()
    #目前会在用户退出后重放一遍刚才创作的乐曲
    #可以在创作界面设置一个“自己欣赏”按钮来激活这个函数
    print('now replay it')
    drum.replay()
    #在创作界面设置“再来一次”按钮跳回到‘JUMP’处，用循环或go to实现
    #在用户退出程序才需调用
    del eye
    del drum
