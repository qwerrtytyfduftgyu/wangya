#!D:\anconda\envs\py311
# -*- coding: utf-8 -*-
# @Time    : 2024/4/24 下午2:14
# @Author  : 汪雅
# @School  : 厦门华厦学院
# @FileName: 膨胀腐蚀操作.py
# @Software: PyCharm
import cv2
import numpy as np


def Ren(inputfile):
    original = cv2.imread(inputfile)
    # bushifire = cv2.imread('bushfire.png')
    gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
    t, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    k = np.ones((5, 5), np.uint8)
    tidu = cv2.morphologyEx(binary, cv2.MORPH_GRADIENT, k)
    li_mao = cv2.morphologyEx(binary, cv2.MORPH_TOPHAT, k)
    hei_mao = cv2.morphologyEx(binary, cv2.MORPH_BLACKHAT, k)
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    cv2.imshow('original', original)
    cv2.imshow('tidu', tidu)
    cv2.imshow('Li_Mao', li_mao)
    cv2.imshow('Hei_Mao', hei_mao)
    cv2.drawContours(original, contours, -1, (0, 0, 255), 5)
    cv2.imshow("img", original)
    cv2.waitKey()
    cv2.destroyAllWindows()


def hougt(inputfile):
    original = cv2.imread(inputfile)
    img = original.copy()

    img = cv2.medianBlur(img, 5)
    gray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
    binary = cv2.Canny(img, 50, 100)
    lines = cv2.HoughLinesP(binary, 1, np.pi / 180)


if __name__ == "__main__":
    try:
        Ren('ren.png')

    except :
        print("代码出错了！！！")
    finally:
        pass
