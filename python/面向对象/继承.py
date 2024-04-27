#!D:\anconda\envs\py311
# -*- coding: utf-8 -*-
# @Time    : 2024/4/20 下午4:51
# @Author  : 汪雅
# @School  : 厦门华厦学院
# @FileName: 继承.py
# @Software: PyCharm
class fu:
    def func(self):
        print("func.self")

    def mes(self):
        print("fu.mes.self")


class zi(fu):
    pass
    # def mes(self):
    #     print("mes.self")


# s = zi()
# s.func()
# s.mes()

class base:
    def f1(self):
        print('sfbuzubfzs')
        self.f3()
        print('sffs')

    def f2(self):
        print('123456')


class foo():
    def f2(self):
        print('wangya')

    def f3(self):
        print('sadad')

class Be(base,foo):
    def f1(self):
        print("xsfa")
        self.f2()

def run():
    a = Be()
    a.f1()


if __name__ == "__main__":
    try:
        run()
    except:
        print("上面的程序有错！！！")
    finally:
        print("程序执行完毕！")
