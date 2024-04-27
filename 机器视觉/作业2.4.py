#!D:\anconda\envs\py311
# -*- coding: utf-8 -*-
# @Time    : 2024/4/17 下午3:29
# @Author  : 汪雅
# @School  : 厦门华厦学院
# @FileName: 作业2.4.py
# @Software: PyCharm
'''
  新能源汽车车牌号以绿色为主，包括小型新能源汽车专用车牌和大型新能源汽车专用车牌，尺寸为 48cm ；14厘米。
'''
import cv2
import numpy as np
a = cv2.imread('car.png',1)
# a = cv2.resize(a,(500,500))
W,H,C = a.shape
roi = cv2.selectROI("roi",a,True,False)
x,y,w,h = roi
img_roi = a[int(y):int(y+h),int(x):int(x+w)]
cv2.destroyAllWindows()
a = cv2.imread('car.png',1)
cv2.rectangle(img=a,pt1=(x,y),pt2=(x+w,y+h),color=(0,0,255),thickness=2)
roi1 = cv2.selectROI("roi",a,True,False)
x1,y1,w1,h1 = roi
img_roi1 = a[int(y1):int(y1+h1),int(x1):int(x1+w1)]
cv2.rectangle(img=a,pt1=(x1,y1),pt2=(x1+w1,y1+h1),color=(0,0,255),thickness=2)
cv2.destroyAllWindows()
chang = np.sqrt(w1*w1+h1*h1)
kuan = 7*chang/24
P1 = np.zeros((4,2),np.float32)
P1[0] = [x,y]
P1[1] = [x+w,y+h]
P1[2] = [x1,y1]
P1[3] = [x1+w1,y1+h1]
P2 = np.zeros((4,2),np.float32)
# P2[0] = [0,H-kuan]
# P2[1] = [chang,H-kuan]
# P2[2] = [0,H]
# P2[3] = [chang,H]
P2[0] = [0,0]
P2[1] = [w,0]
P2[2] = [0,h]
P2[3] = [w,h]
M = cv2.getPerspectiveTransform(P1,P2)
dst = cv2.warpPerspective(a,M,(W,H))
cv2.imshow('a',a)
cv2.imshow('dst',dst)
cv2.waitKey()
cv2.destroyAllWindows()

