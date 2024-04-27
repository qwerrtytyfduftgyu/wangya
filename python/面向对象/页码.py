#!D:\anconda\envs\py311
# -*- coding: utf-8 -*-
# @Time    : 2024/4/20 下午3:25
# @Author  : 汪雅
# @School  : 厦门华厦学院
# @FileName: 页码.py
# @Software: PyCharm
class Page:
    def __init__(self,Current_page,per_page_name=10):
        self.per_page_name = per_page_name
        if not Current_page.isdecimal():
            self.Current_page = 1
        if int(Current_page) < 1:
            self.Current_page = 1
            return
        self.Current_page = int(Current_page)

    def start(self):
        return (self.Current_page-1) * self.per_page_name
    def end(self):
        return self.Current_page * self.per_page_name


user_input = ["用户-{}".format(i) for i in range(1,300)]
while True:
    page = input("请输入页码：")
    PG_object = Page(page,10)
    page_data_list = user_input[PG_object.start():PG_object.end()]
    if int(page) <= -100:
        break
    for item in page_data_list:
        print(item)