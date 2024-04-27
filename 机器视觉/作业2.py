#!D:\anconda\envs\py311
# -*- coding: utf-8 -*-
# @Time    : 2024/4/3 14:05
# @Author  : 汪雅
# @School  : 厦门华厦学院
# @FileName: 作业2.py
# @Software: PyCharm
import cv2
import numpy as np
img1 = cv2.imread("2.bmp",1)
img1 = cv2.resize(img1,(500,500))
img2 = cv2.imread("girl.bmp",1)
img2 = cv2.resize(img2,(500,500))
sum1 = img1 + img2
b = np.zeros(img2.shape,dtype=np.uint8)
b[0:500,200:300]=255
b[200:300,0:500]=255
c = cv2.bitwise_and(img2,b)
cv2.imshow("1",img2)
cv2.imshow("2",b)
cv2.imshow("3",c)
print(f"sum1={sum1}" )
cv2.imshow("sum1",sum1)
cv2.waitKey()
cv2.destroyAllWindows()
