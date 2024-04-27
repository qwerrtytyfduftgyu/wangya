#!D:\anconda\envs\py311
# -*- coding: utf-8 -*-
# @Time    : 2024/4/10 下午1:46
# @Author  : 汪雅
# @School  : 厦门华厦学院
# @FileName: 作业2.1.py
# @Software: PyCharm
import cv2
import numpy as np
a = cv2.imread("2.bmp",cv2.IMREAD_UNCHANGED)
a = cv2.resize(a,(500,500))
roi = cv2.selectROI("roi",a,True,False)
x,y,w,h = roi
print(x,y,w,h)
img_roi = a[int(y):int(y+h),int(x):int(x+w)]
cv2.rectangle(img=a,pt1=(x,y),pt2=(x+w,y+h),color=(0,0,255),thickness=2)
face = np.random.randint(0,256,(h,w,3))
# face1 = a[int(y):int(y+h),int(x):int(x+w)]
cv2.imshow('mingan2',img_roi)
a[int(y):int(y+h),int(x):int(x+w)]=face
cv2.imshow('mingan',a)
# cv2.imshow('yuantu',b)
# cv2.imshow("imageHSV",img_roi)
cv2.waitKey( )
cv2.destroyAllWindows()
