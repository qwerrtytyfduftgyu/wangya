#!D:\anconda\envs\py311
# -*- coding: utf-8 -*-
# @Time    : 2024/4/10 下午2:39
# @Author  : 汪雅
# @School  : 厦门华厦学院
# @FileName: 作业2.2.py
# @Software: PyCharm
import cv2
import numpy as np
import matplotlib.pyplot as plt
"""
灰度变换包括线性灰度变幻、分段线性灰度变换、非线性灰度变换、直方图均衡化
     （非线性灰度变换包括对数变换、伽马变换)
"""
# 下面是线性灰度变换的代码：
# img = cv2.imread('2.bmp',0)
# heights = img.shape[0]
# width = img.shape[1]
# result = np.zeros([heights,width],np.uint8)
# for i in range(heights):
#     for j in range(width):
#         gray = 255-img[i,j]
#         result[i,j] = np.uint8(gray)
# cv2.imshow("Gray Image",img)
# cv2.imshow("Result",result)
# cv2.waitKey( )
# cv2.destroyAllWindows()
# 下面是分段线性灰度变换的代码
# img = cv2.imread("2.bmp",0)
# img = cv2.resize(img,(500,500))
# x1 = int(input("请输入第一个坐标点的横坐标x1："))
# y1 = int(input("请输入第一个坐标点的横坐标y1："))
# x2 = int(input("请输入第一个坐标点的横坐标x2："))
# y2 = int(input("请输入第一个坐标点的横坐标y2："))
# for i in range(img.shape[0]):
#     for j in range(img.shape[1]):
#       if img[i,j] > 255:
#           img[i,j] = 255
#       if img[i,j] < 0:
#           img[i,j] = 0
# result = np.zeros((img.shape[0],img.shape[1]),np.uint8)
# k1 = y1 / x1
# k2 = (y2-y1) / (x2-x1)
# k3 = (255-y2) / (255-x2)
# for i in range(img.shape[0]):
#     for j in range(img.shape[1]):
#         if img[i,j] < x1:
#             result[i,j] = k1 * (img[i,j])
#         if x1 < img[i,j] < x2:
#             result[i,j] = k2 * (img[i,j]-x1)+y1
#         if img[i,j] > x2:
#             result[i,j] = k3 * (img[i,j]-x2)+y2
# cv2.imshow('gray',img)
# cv2.imshow("result image",result)
# cv2.waitKey( )
# cv2.destroyAllWindows()
# 下面是非线性灰度变换的代码,包括对数变换和伽马变换
"下面是对数变换的代码"
# img = cv2.imread("2.bmp",0)
# img = cv2.resize(img,(500,500))
# c = 0.05
# # 这两行不太懂什么意思，而且还报错
# result = c * np.log(1+img)# 对数变换
# result = np.uint8(result+0.5)
# #
# cv2.imshow('gray',img)
# cv2.imshow("result image",result)
# cv2.waitKey( )
# cv2.destroyAllWindows()
# 下面是非线性灰度变换的代码,包括对数变换和伽马变换
"下面是伽马变换的代码"
# img = cv2.imread('2.bmp',0)
# c,gamma = 0.005,2
# result = np.zeros((img.shape[0],img.shape[1]),np.float32)
# for i in range(img.shape[0]):
#     for j in range(img.shape[1]):
#         result[i,j] = c * np.power(img[i,j],gamma)
# cv2.imshow('gray',img)
# cv2.imshow("result image",result)
# cv2.waitKey( )
# cv2.destroyAllWindows()
# 下面是直方图均衡化的代码
img = cv2.imread('2.bmp',0)
img = cv2.resize(img,(500,500))
equ = cv2.equalizeHist(img)
cv2.imshow("original",img)
cv2.imshow("result",equ)
plt.figure("原始图像与均衡化结果对比直方图")
plt.subplot(1,2,1)
plt.hist(img.ravel(),256,density=True)
plt.xlabel('Value',fontdict={'family':'SimHei','size':'16'})
plt.ylabel('Frequency',fontdict={'family':'SimHei','size':'16'})
plt.title('ChuShiZhiFangTu')
plt.subplot(1,2,2)
plt.hist(equ.ravel(),256,density=True)
plt.xlabel('Value',fontdict={'family':'SimHei','size':'16'})
plt.ylabel('Frequency',fontdict={'family':'SimHei','size':'16'})
plt.title('JunHengHuaZhiFangTu')
plt.show()
plt.tight_layout()
cv2.waitKey( )
cv2.destroyAllWindows()


