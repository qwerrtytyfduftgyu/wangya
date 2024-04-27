#!D:\anconda\envs\py311
# -*- coding: utf-8 -*-
# @Time    : 2024/4/18 下午12:50
# @Author  : 汪雅
# @School  : 厦门华厦学院
# @FileName: class类.py
# @Software: PyCharm
'''
这是第三次学习面向对象，希望能够得到更多的理解吧！！！！
'''

class Message:
    def __init__(self,content):
        self.data = content
    def dayin(self,name):
        print(f'给{name}发邮件,他的邮箱是{self.data}')


# A = Message("210373113@QQ.com")
# print(A.dayin('汪雅'))
class Info :
    """所有员工的基类"""
    def __init__(self,name,password):
        self.name = name
        self.password = password


def run():
    object_shuju_list = []
    while 1:
        name = input("请输入您的用户名(按下Q结束)：")
        password = input("请输入您的密码(按下Q结束)：")
        if name.upper() == "Q":
            break
        userinfo = Info(name,password)
        object_shuju_list.append(userinfo)

        for i in object_shuju_list:
            print(i.name,i.password)

run()