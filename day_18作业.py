# 在作业文件同级目录下
# 1.创建一个文件夹,test
# 2.将文件夹test更名为haha
# 3.在haha文件夹中创建1个txt文件,test.txt
# 4.在test.txt中写入:
#                 鹅鹅鹅
#                 曲项向天歌
#                 白毛浮绿水
#                 红掌拨清波
# 5.再在haha文件夹下新建2个txt文件abc.txt和edf.txt,
# 将test.txt中的字符数低于5的行写入abc.txt,其余的写入edf.txt
# 6.获取haha文件夹中的目录列表,并且写入到test.txt中(另起一行)
# 所有操作全部写在作业文件中,可以一步全部运行生成

# 注意提交作业截图的时候，除了代码和运行结果截图，需要把abc.txt，edf.txt，test.txt三个文件的内容也截图哦！
import os
os.mkdir('2')
os.rename('2', '1')
with open('text.txt', 'w',encoding='utf-8') as f:
    f.write("鹅鹅鹅\n曲项向天歌\n白毛浮绿水\n红掌拨清波")
with (open('abc.txt', 'w',encoding='utf-8') as a,
    open('edf.txt', 'w',encoding='utf-8') as b):
        for line in open('text.txt','r',encoding='utf-8'):
            newline=line.rstrip('\n')
            content=len(newline)
            if content<5:
                a.write(newline)
            else:
                b.write(newline+'\n')
path= '1'
items=os.listdir(path)
with open('text.txt','r',encoding='utf-8') as f:
    for line in items:
        f.write(line+'\n')







