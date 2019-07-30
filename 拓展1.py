def func_2(name):
    f=open('namefile.txt','r')
    dicfile = open('storagedic.txt', 'r+')
    dic=dicfile.readlines()
    number_list=f.readlines()
    for i in number_list:
        # 对文件合并操作
        newfile = open(name, 'ab')
        f = open(dic[i], 'rb')
        newfile.write(f.read())
        f.close()
        newfile.flush()
        newfile.close()
    f.close()
    dicfile.close()



