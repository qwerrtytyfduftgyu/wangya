#!D:\anconda\envs\py311
# -*- coding: utf-8 -*-
# @Time    : 2024/4/10 下午9:29
# @Author  : 汪雅
# @School  : 厦门华厦学院
# @FileName: zuoye2.2.py
# @Software: PyCharm
import cv2
import numpy as np
img1 = cv2.imread('2.bmp',1)
img1 = cv2.resize(img1,(500,500))
img2 = cv2.imread('girl.bmp',1)
img2 = cv2.resize(img2,(500,500))
roi = cv2.selectROI("roi",img1,True,False)
x,y,w,h = roi
cv2.rectangle(img=img1,pt1=(x,y),pt2=(x+w,y+h),color=(0,0,255),thickness=2)
face = np.random.randint(0,256,(h,w,3))
img2[int(y):int(y+h),int(x):int(x+w)] = img1[int(y):int(y+h),int(x):int(x+w)]
cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.waitKey( )
cv2.destroyAllWindows()

