#!D:\anconda\envs\py311
# -*- coding: utf-8 -*-
# @Time    : 2024/4/12 下午2:08
# @Author  : 汪雅
# @School  : 厦门华厦学院
# @FileName: 作业2.3.py
# @Software: PyCharm
import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.resize(cv2.imread('girl.bmp',0),(500,500))
equ = cv2.equalizeHist(img)
GaussianBlur = cv2.GaussianBlur(img,(11,11),0,0)
b = np.zeros(img.shape,dtype=np.uint8)
b[100:400,100:400]=255
# cv2.imshow("b",b)
height,weight = b.shape[:2]
C = (height/2,weight/2)
A = np.sqrt(2)/2
M = cv2.getRotationMatrix2D(C,45,A)
rotate = cv2.warpAffine(b,M,(weight,height))
c = cv2.bitwise_and(img,rotate)
plt.figure("这不是我的作业")
plt.subplot(2,2,1)
plt.imshow(img)
plt.xticks([])
plt.yticks([])
plt.subplot(2,2,2)
plt.hist(equ.ravel(),256,density=True)
plt.xlabel('Value',fontdict={'family':'SimHei','size':'16'})
plt.ylabel('Frequency',fontdict={'family':'SimHei','size':'16'})
plt.title('JunHengHuaZhiFangTu')
plt.subplot(2,2,3)
plt.imshow(GaussianBlur)
plt.xticks([])
plt.yticks([])
plt.subplot(2,2,4)
plt.imshow(c)
plt.xticks([])
plt.yticks([])
plt.show()
plt.tight_layout()
cv2.waitKey( )
cv2.destroyAllWindows()


