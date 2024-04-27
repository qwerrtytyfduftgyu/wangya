# f = open('新建 文本文档.txt',mode='r',encoding='UTF-8')
# # f =f.read()
# # print(f)
# F = f.readline().strip()
# print(F)
# F = f.readline()
# print(F)
# for line in f:#最简洁的读取文件里面所有文件的方式
#     print(line.strip())
#

# lst = ['张三','李四','王五']#在文件中写入这几个人名
# f = open('嫩模.txt',mode='w',encoding='utf-8')
# for i in lst:
#      f.write(i+"\n"
#      f.close()

# f = open('嫩模.txt',mode='a',encoding='utf-8')
# f.write('你太厉害了')

#with
# with open('嫩模.txt',mode='r',encoding='utf-8') as f:
#     for i in f:
#         print(i.strip())

# with open('行人视频.mp4',mode='rb') as f1:#读写非文本内容时要加b
#     for i in f1:
#         print(i)

# with open('行人视频.mp4',mode='rb') as f,\
#     open('../行人视频1.MP4',mode='wb') as f1:
#         for i in f:
#             f1.write(i)
import  os # 和操作系统相关的模块导入
import time#和时间相关的模块
with open('人名字.txt',mode='r',encoding='utf-8') as f,\
    open('人名字_副本.txt', mode='w', encoding='utf-8') as f1:
    for i in f:
        i = i.strip()
        if i.startswith('周'):
            i = i.replace('周','张')

        f1.write(i)
        f1.write('\n')
time.sleep(3)
os.remove('人名字.txt')
time.sleep(3)
os.rename('人名字_副本.txt', '人名字.txt')