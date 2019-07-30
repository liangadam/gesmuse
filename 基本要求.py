number_list=[]
def func_1(number_present):
    #加入输入的数字，形成列表，准备在func2中拼接音频
    number_list.append(number_present)
    import os
    namelist = []
    dicfile=open('storagedic.txt','a+')
    namefile=open('namefile.txt','a+')
    namefile.write(number_present + os.linesep)
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
        for j in range(10):
            dic[j] = namelist[j]
        print(dic)
    else:
        dic=eval(dic)
    dicfile.close()
    #播放音乐
    import simpleaudio as sa
    number = int(number_present,2)
    filename = dic[number]
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()  # Wait until sound has finished playing
    namefile.close()
    #作为整个函数func_1的返回值，用于func_3的调用
    return dic