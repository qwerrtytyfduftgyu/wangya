#!D:\anconda\envs\py311
# -*- coding: utf-8 -*-
# @Time    : 2024/4/23 下午8:06
# @Author  : 汪雅
# @School  : 厦门华厦学院
# @FileName: 多态.py
# @Software: PyCharm
class shaboyi:
    name1 = "cxx"
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def yuw(self):
        pass

    def afa(cls):
        pass

a = shaboyi("wy",18,0)
print(a.name1)
print(shaboyi.afa())