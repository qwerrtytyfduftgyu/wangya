#!D:\anconda\envs\py311
# -*- coding: utf-8 -*-
# @Time    : 2024/4/8 下午10:45
# @Author  : 汪雅
# @School  : 厦门华厦学院
# @FileName: 爱心.py
# @Software: PyCharm

import tkinter as tk
import tkinter.messagebox
import random
from math import sin, cos, pi, log
from tkinter.constants import *

# 设置画布的宽度和高度
width = 888
height = 500

# 爱心中心的坐标
heartx = width / 2
hearty = height / 2

# 爱心的大小
side = 11

# 爱心颜色，可修改
heartcolor = "pink"


class Heart:
    def __init__(self, generate_frame=20):
        # 原始爱心坐标集合
        self._points = set()

        # 边缘扩散效果点坐标集合
        self._edge_diffusion_points = set()

        # 中心扩散效果点坐标集合
        self._center_diffusion_points = set()

        # 每帧动态点坐标
        self.all_points = {}

        # 创建爱心坐标集合
        self.build(2000)

        # 设置随机光晕大小
        self.random_halo = 1000
        self.generate_frame = generate_frame

        # 计算每一帧的爱心坐标
        for frame in range(generate_frame):
            self.calc(frame)

    def build(self, number):
        # 生成原始爱心坐标
        for _ in range(number):
            t = random.uniform(0, 2 * pi)
            x, y = heart_function(t)
            self._points.add((x, y))

        # 生成边缘扩散效果点坐标
        for _x, _y in list(self._points):
            for _ in range(3):
                x, y = scatter_inside(_x, _y, 0.05)
                self._edge_diffusion_points.add((x, y))

        point_list = list(self._points)

        # 生成中心扩散效果点坐标
        for _ in range(4000):
            x, y = random.choice(point_list)
            x, y = scatter_inside(x, y, 0.17)
            self._center_diffusion_points.add((x, y))

    @staticmethod
    def calc_position(x, y, ratio):
        # 计算每个点的位置
        force = 1 / (((x - heartx) ** 2 + (y - hearty) ** 2) ** 0.520)
        dx = ratio * force * (x - heartx) + random.randint(-1, 1)
        dy = ratio * force * (y - hearty) + random.randint(-1, 1)
        return x - dx, y - dy

    def calc(self, generate_frame):
        # 计算每一帧的爱心坐标
        ratio = 10 * curve(generate_frame / 10 * pi)
        halo_radius = int(4 + 6 * (1 + curve(generate_frame / 10 * pi)))
        halo_number = int(3000 + 4000 * abs(curve(generate_frame / 10 * pi) ** 2))
        all_points = []
        heart_halo_point = set()

        # 生成光晕坐标
        for _ in range(halo_number):
            t = random.uniform(0, 2 * pi)
            x, y = heart_function(t, shrink_ratio=11.6)
            x, y = shrink(x, y, halo_radius)
            if (x, y) not in heart_halo_point:
                heart_halo_point.add((x, y))
                x += random.randint(-14, 14)
                y += random.randint(-14, 14)
                size = random.choice((1, 2, 2))
                all_points.append((x, y, size))

        # 计算原始爱心坐标
        for x, y in self._points:
            x, y = self.calc_position(x, y, ratio)
            size = random.randint(1, 3)
            all_points.append((x, y, size))

        # 计算边缘扩散效果点坐标
        for x, y in self._edge_diffusion_points:
            x, y = self.calc_position(x, y, ratio)
            size = random.randint(1, 2)
            all_points.append((x, y, size))

        # 计算中心扩散效果点坐标
        for x, y in self._center_diffusion_points:
            x, y = self.calc_position(x, y, ratio)
            size = random.randint(1, 2)
            all_points.append((x, y, size))

        self.all_points[generate_frame] = all_points

    def render(self, render_canvas, render_frame):
        # 渲染爱心
        for x, y, size in self.all_points[render_frame % self.generate_frame]:
            render_canvas.create_rectangle(x, y, x + size, y + size, width=0, fill=heartcolor)


def heart_function(t, shrink_ratio: float = side):
    # 爱心函数
    x = 16 * (sin(t) ** 3)
    y = -(13 * cos(t) - 5 * cos(2 * t) - 2 * cos(3 * t) - cos(4 * t))
    x *= shrink_ratio
    y *= shrink_ratio
    x += heartx
    y += hearty
    return int(x), int(y)


def scatter_inside(x, y, beta=0.15):
    # 计算内部扩散坐标
    ratio_x = - beta * log(random.random())
    ratio_y = - beta * log(random.random())
    dx = ratio_x * (x - heartx)
    dy = ratio_y * (y - hearty)
    return x - dx, y - dy


def shrink(x, y, ratio):
    # 收缩爱心
    force = -1 / (((x - heartx) ** 2 + (y - hearty) ** 2) ** 0.6)
    dx = ratio * force * (x - heartx)
    dy = ratio * force * (y - hearty)
    return x - dx, y - dy


def curve(p):
    # 计算曲线
    return 2 * (2 * sin(4 * p)) / (2 * pi)


def draw(main: tk.Tk, render_canvas: tk.Canvas, render_heart: Heart, render_frame=0):
    # 绘制爱心
    render_canvas.delete('all')
    render_heart.render(render_canvas, render_frame)
    main.after(160, draw, main, render_canvas, render_heart, render_frame + 1)


def love():
    # 创建窗口
    root = tk.Tk()
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    x = (screenwidth - width) // 2
    y = (screenheight - height) // 2 - 66
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.title("❤")
    canvas = tk.Canvas(root, bg='black', height=height, width=width)
    canvas.pack()
    heart = Heart()
    draw(root, canvas, heart)
    tk.Label(root, text="I Love You!", bg="black", fg="#FF99CC", font="Helvetic 25 bold").place(relx=.5, rely=.5,
                                                                                                anchor=CENTER)
    root.mainloop()


if __name__ == '__main__':
    # 创建主窗口
    root = tk.Tk()
    root.title('嘻嘻')
    root.resizable(0, 0)
    root.wm_attributes("-toolwindow", 1)
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    widths = 300
    heights = 100
    x = (screenwidth - widths) / 2
    y = (screenheight - heights) / 2 - 66
    root.geometry('%dx%d+%d+%d' % (widths, heights, x, y))  # 设置在屏幕中居中显示

    # 创建标签和按钮
    tk.Label(root, text='亲爱的，做我女朋友好吗？', width=37, font=('宋体', 12)).place(x=0, y=10)


    def OK():  # 同意按钮
        root.destroy()
        love()  # 同意后显示动态爱心


    def NO():  # 拒绝按钮，拒绝不会退出，必须同意才可以退出哦~
        tk.messagebox.showwarning('❤', '再给你一次机会！')


    def closeWindow():
        tk.messagebox.showwarning('❤', '逃避是没有用的哦')


    tk.Button(root, text='好哦', width=5, height=1, command=OK).place(x=80, y=50)
    tk.Button(root, text='不要', width=5, height=1, command=NO).place(x=160, y=50)
    root.protocol('WM_DELETE_WINDOW', closeWindow)  # 绑定退出事件
    root.mainloop()