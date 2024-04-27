#!D:\anconda\envs\py311
# -*- coding: utf-8 -*-
# @Time    : 2024/3/31 16:16
# @Author  : 汪雅
# @School  : 厦门华厦学院
# @FileName: Leetcode279.py
# @Software: PyCharm

class Solution: #动态规划方法
    def numSquares(self,n):
        square = [i*i for i in range(1,101)]
        dp = [float("inf")] * (n+1)
        dp[0] = 0
        for i in range(1,n+1):
            for j in square:
                if j <= i:
                    dp[i] = min(dp[i],dp[i-j]+1)
        return dp[n]

a = Solution()
print(a.numSquares(104))