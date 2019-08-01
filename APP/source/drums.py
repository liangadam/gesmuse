#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' drums '

__auther__ = 'wlp'
import os

number_list = []
import simpleaudio as sa
import time


class Drums(object):
    def __init__(self, address):
        self.address = address  # 音响文件地址
        self.temp = []
        dic = {}
        namelist = []
        f_list = os.listdir(address)
        # print f_list
        for i in f_list:
            # os.path.splitext():分离文件名与扩展名
            if os.path.splitext(i)[1] == '.wav':
                # print(i)
                namelist.append(i)
        self.obj = []
        for j in range(len(namelist)):
            obj = sa.WaveObject.from_wave_file(self.address + namelist[j])
            self.obj.append(obj)
        # 需要外界输入
        self.ges = [30, 31, 6, 7]
        self.txt = 'temp.txt'

    def beat(self, number):
        if number in self.ges:
            order = self.ges.index(number)
            self.temp.append(order)

            play_obj = self.obj[order].play()
        # play_obj.wait_done()  # Wait until sound has finished playing

    def store(self):
        f = open(self.txt, 'w')
        f.write('')
        f.close()
        f = open(self.txt, 'a')
        for x in self.temp:
            f.write('%d ' % x)
        f.close()
        self.temp = []

    def replay(self):
        f = open(self.txt, 'r')
        temp1 = f.readline()
        number_list = [int(x) for x in temp1.split()]
        for i in number_list:
            play_obj = self.obj[i].play()
            time.sleep(1)
        f.close()
        return 1


'''         
def func_1(number_present):
    #加入输入的数字，形成列表，准备在func2中拼接音频
    number_list.append(number_present)
    namelist = []
    dicfile=open('storagedic.txt','a+')
    namefile=open('namefile.txt','a+')
    namefile.write('%d '%number_present)
    dic=dicfile.read()
    if dic=='':
        dic = {}
        f_list = os.listdir('./sound/')
        # print f_list
        for i in f_list:
            # os.path.splitext():分离文件名与扩展名
            if os.path.splitext(i)[1] == '.wav':
                print(i)
                namelist.append(i)
        print(namelist)
        for j in range(10):
            dic[j] = namelist[j]
        print(dic)
        
    else:
        dic=eval(dic)
    dicfile.close()
    #播放音乐
    
    number = int(number_present)
    filename = dic[number]
    wave_obj = sa.WaveObject.from_wave_file('./sound/'+filename)
    play_obj = wave_obj.play()
    #play_obj.wait_done()  # Wait until sound has finished playing
    namefile.close()
    #作为整个函数func_1的返回值，用于func_3的调用
    return dic

def func_2(name):
    f=open('namefile.txt','r')
    dicfile = open('storagedic.txt', 'r+')
    dic=dicfile.read()
    temp1=f.readline()
    number_list=[int(x) for x in temp1.split()]
    print(number_list)
    for i in number_list:
        # 对文件合并操作
        newfile = open(name+'.txt', 'ab')
        f = open(dic[i], 'rb')
        newfile.write(f.read())
        f.close()
        newfile.flush()
        newfile.close()
    f.close()
    dicfile.close()

def func_3(filename,number):
    #调用基本要求里面的返回值
    dic=func_1(number_present)
    #原来的列表里面加入新的元素
    dic[number]=filename
'''
