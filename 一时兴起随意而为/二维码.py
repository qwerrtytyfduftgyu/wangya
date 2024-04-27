#!D:\anconda\envs\py311
# -*- coding: utf-8 -*-
# @Time    : 2024/4/26 下午10:40
# @Author  : 汪雅
# @School  : 厦门华厦学院
# @FileName: 二维码.py
# @Software: PyCharm
from pyzbar.pyzbar import decode
from PIL import Image

# 打开图像文件
image = Image.open('123.png')

# 对图像文件进行解码
data = decode(image)

# 打印解码结果
for obj in data:
    print('二维码类型: ', obj.type)
    print('二维码数据: ', obj.data.decode('utf-8'))