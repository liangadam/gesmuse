import os
namelist = []
dicfile=open('storagedic.txt','r+')
dic=dicfile.read()
if dic=='':
    dic = {}
    f_list = os.listdir('/Users/fangke10000/PycharmProjects/何吉波暑校/大作业/')
    # print f_list
    for i in f_list:
        # os.path.splitext():分离文件名与扩展名
        if os.path.splitext(i)[1] == '.wav':
            print(i)
            namelist.append(i)
    print(namelist)
    for j in range(32):
        dic[j] = namelist[j]
    print(dic)
else:
    dic=eval(dic)
dicfile.close()
print(dic)


import simpleaudio as sa
judgement=True
counttimesfile=open('storage.txt','r+')
print(type(counttimesfile.read()))
if counttimesfile.read()=='':
    counttimes = 0

else:
    counttimes=counttimesfile.read()
counttimesfile.close()

# counttimeslist是对于每一次运行py文件，所生成的次数形成的列表
if len(dic)==32:
    while judgement:
        number = int(input(),2)
        if number == -1:
            break
        else:
            # newlist是基本要求里面input的字符对应的每个元素按照顺序形成的列表，用于生成新的音频文件
            newlist = []
            newlist.append(number)
            filename = dic[number]
            wave_obj = sa.WaveObject.from_wave_file(filename)
            play_obj = wave_obj.play()
            play_obj.wait_done()  # Wait until sound has finished playing

            # 对文件合并操作
            newfile = open(f'newfile_{counttimes}.wav', 'ab')
            for numbers in newlist:
                f = open(dic[numbers], 'rb')
                newfile.write(f.read())
                f.close()
            newfile.flush()
            newfile.close()
            tempratenum=int(counttimes)
            tempratenum += 1
            counttimes=str(tempratenum)
        dic[31+tempratenum]=f'newfile_{counttimes}.wav'
else:
    while judgement:
        number = input()
        numberlist=number.split(',')
        numberlist=[int(i) for i in numberlist]
        print(numberlist)
        if number == '-1':
            break
        else:
            # newlist是基本要求里面input的字符对应的每个元素按照顺序形成的列表，用于生成新的音频文件
            newlist = []
            for k in numberlist:
                newlist.append(int(k))
                filename = dic[int(k)]
                wave_obj = sa.WaveObject.from_wave_file(filename)
                play_obj = wave_obj.play()
                play_obj.wait_done()  # Wait until sound has finished playing

            # 对文件合并操作
            newfile = open(f'newfile_{counttimes}.wav', 'ab')
            for numbers in newlist:
                f = open(dic[numbers], 'rb')
                newfile.write(f.read())
                f.close()
            newfile.flush()
            newfile.close()
            tempratenum = int(counttimes)
            tempratenum += 1
            counttimes = str(tempratenum)
        dic[31 + tempratenum] = f'newfile_{counttimes}.wav'



# counttimesfile是对于counttimes形成的列表
counttimesfile = open('storage.txt', 'w+')
counttimesfile.write(counttimes)
counttimesfile.close()

storagedic=open('storagedic.txt','w+')
storagedic.write(str(dic))
storagedic.close()
print(dic)













