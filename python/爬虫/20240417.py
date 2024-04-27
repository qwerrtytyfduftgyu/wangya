#!D:\anconda\envs\py311
# -*- coding: utf-8 -*-
# @Time    : 2024/4/17 下午8:03
# @Author  : 汪雅
# @School  : 厦门华厦学院
# @FileName: 20240417.py
# @Software: PyCharm
url = "https://www.hongxiu.com/chapter/18899519001291804/50733067052494681"
import requests
from lxml import etree
#使用etree方法解析保留住html源码
# .content 获取二进制数据
# .text获取源码
response = requests.get(url)#网络源码
htmldm = etree.HTML(response)
file = open('1.txt','w',encoding="UTF-8")
for i in a:
    a = htmldm.xpath()
    file.write(a)
    file.write()