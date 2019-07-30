#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' drums '

__auther__='wlp'

number_list=[]
def func_1(number_present):
    #加入输入的数字，形成列表，准备在func2中拼接音频
    number_list.append(number_present)
    import os
    namelist = []
    dicfile=open('storagedic.txt','a+')
    namefile=open('namefile.txt','a+')
    namefile.write('%d'%number_present)
    dic=dicfile.read()
    if dic=='':
        dic = {}
        f_list = os.listdir('d:/python/gesmuse/drums/gesmuse_drums')
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
    import simpleaudio as sa
    number = int(number_present)
    filename = dic[number]
    wave_obj = sa.WaveObject.from_wave_file('d:/python/gesmuse/drums/gesmuse_drums/'+filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()  # Wait until sound has finished playing
    namefile.close()
    #作为整个函数func_1的返回值，用于func_3的调用
    return dic

def func_2(name):
    f=open('namefile.txt','r')
    dicfile = open('storagedic.txt', 'r+')
    dic=dicfile.readlines()
    number_list=f.readlines()
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

if __name__== '__main__':
    func_1(1)
    func_1(2)
    func_2('first')
