#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/3/31 14:26
# @Author  : 汪雅
# @School  : 厦门华厦学院
# @FileName: class__继承.py
# @Software: PyCharm
"""
这是一些关于类的继承的一些代码
类的属性 vs 对象的属性
类的属性对象也可以调用
对象的属性形同  self.xxxxx
"""
class Animal:
     popultion = True
     def __init__(self,name,age):
         self.name = name
         self.__age = age
         #self.__age = age#在类的属性前面加__可以不被子类继承
     def eat(self):
         print("这是animal的eat函数")
     def sound(self):
         pass
     @classmethod#装饰器 将对象的函数变为类的函数
     def piss(self):
         print("尿尿")
class Dog(Animal):
    def __init__(self):
        super().__init__("旺财",20)# 子类传参数到父类
        pass
    def sound(self):
        print("汪汪汪")

class Cat(Animal):
    def __init__(self):
        super().__init__("糯米",20)# 子类传参数到父类
        pass
    def sound(self):
        print("喵喵喵")
def makesound(Animal):
    Animal.sound()
dog = Dog()#创建基于Dog对象的实例
cat = Cat()#创建基于Cat对象的实例
# dog.eat()
# print(dog.name)
makesound(dog)
makesound(cat)
A1 = Animal(1,2)
A2 = Animal(1,2)
print(Animal.popultion)
print(A1.popultion)
print(id(A1.sound))
Animal.piss()
