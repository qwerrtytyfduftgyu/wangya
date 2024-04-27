#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/3/31 14:20
# @Author  : 汪雅
# @School  : 厦门华厦学院
# @FileName: class.py
# @Software: PyCharm
"""
第二次学习类
类 对象 类是具有相同特征的一些对象的模板
面向对象编程三大特性 封装 继承 多态
    封装：把共性(属性，函数)搞在一起变成个类
    继承：子类继承父类的属性，函数
    多态：同一个名字的函数，拥有不同的效果
"""

class CaiXuKun:
    def __init__(self,name,age,sex,OtherName,ktc,zwjs):
        self.xm = name  #让对象拥有一个名叫xm的属性
        self.age = age
        self.sex = sex
        self.OtherName = OtherName
        self.ktc = ktc
        self.zwjs = zwjs
    def koutouchan(self):
        print(self.ktc)
    def ziwojieshao(self):
        print(self.zwjs)


People = CaiXuKun("蔡徐坤",23,"男","鸡哥","你干嘛哎呦","练习时长两年半")
People.koutouchan()
People.ziwojieshao()
print(People.xm)
