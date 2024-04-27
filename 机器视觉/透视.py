#!D:\anconda\envs\py311
# -*- coding: utf-8 -*-
# @Time    : 2024/4/17 下午7:09
# @Author  : 汪雅
# @School  : 厦门华厦学院
# @FileName: 透视.py
# @Software: PyCharm
import cv2
import numpy as np

# 读取图像
image = cv2.imread('car.png')
W,H,C = image.shape

# 创建一个窗口并在其中显示图像
cv2.imshow('Select ROIs', image)

# 选择感兴趣区域
rois = []
while True:
    roi = cv2.selectROI('Select ROIs', image, fromCenter=False, showCrosshair=True)
    if roi[2] > 0 and roi[3] > 0:  # 确保选择的ROI是有效的
        rois.append(roi)
    else:
        break

cv2.destroyAllWindows()
x = rois[0][0]
y = rois[0][1]
w = rois[0][2]
h = rois[0][3]
x1 = rois[1][0]
y1 = rois[1][1]
w1 = rois[1][2]
h1 = rois[1][3]
# print(rois)
# print(rois[0][0])
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
dst = cv2.warpPerspective(image,M,(W,H))
cv2.imshow('a',image)
cv2.imshow('dst',dst)
cv2.waitKey()
cv2.destroyAllWindows()

# # 显示选取的感兴趣区域
# for i, roi in enumerate(rois):
#     x, y, w, h = roi
#     selected_roi = image[y:y+h, x:x+w]
#     cv2.imshow(f'ROI {i+1}', selected_roi)

cv2.waitKey(0)
cv2.destroyAllWindows()
