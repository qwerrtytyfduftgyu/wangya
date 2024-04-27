#!D:\anconda\envs\py311
# -*- coding: utf-8 -*-
# @Time    : 2024/4/20 下午3:54
# @Author  : 汪雅
# @School  : 厦门华厦学院
# @FileName: 警察抓小偷.py
# @Software: PyCharm
class Police:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        if self.role == '队长':
            self.HP = 500
        else:
            self.HP = 300

    def show_status(self):
        message = (f"警察{self.name}的血量为{self.HP}")
        print(message)

    def bomb(self, terrorist_list):
        for terrorist in terrorist_list:
            terrorist.blood -= 200
            terrorist.show_status()


class Terroist:
    def __init__(self, name, blood=300):
        self.name = name
        self.blood = blood

    def shoot(self, police_list):
        police_list.HP -= 5
        self.blood -= 1
        police_list.show_status()
        self.show_status()

    def show_status(self):
        message = (f"恐怖分子{self.name}的血量为{self.blood}")
        print(message)


def run():
    p1 = Police("张三", '队长')
    p2 = Police("李四", '')
    p3 = Police("王五", '')
    t1 = Terroist("A")
    t2 = Terroist("B")
    p1.bomb([t2])
    t1.shoot(p2)


if __name__ == "__main__":
    run()
