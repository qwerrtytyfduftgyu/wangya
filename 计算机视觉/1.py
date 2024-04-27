#!D:\anconda\envs\py311
# -*- coding: utf-8 -*-
# @Time    : 2024/4/13 下午7:38
# @Author  : 汪雅
# @School  : 厦门华厦学院
# @FileName: 1.py
# @Software: PyCharm
import numpy as np
class NeareatNeighbor:
    def __init__(self):
        pass

    def train(self,x,y):
        self.xtr = x
        self.ytr = y

    def predict(self,X):
        num_test = X.shape[0]
        Ypred = np.zeros(num_test,dtype = self.ytr.dtype)

        for i in range(num_test):
            distances = np.sum(np.abs(self.Xtr-X[i,:]),axis=1)
            min_index = np.argmin(distances)
            Ypred[i] = self.ytr[min_index]
        return Ypred