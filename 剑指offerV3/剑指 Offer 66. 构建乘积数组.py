# -*- coding:utf-8 -*-
__author__ = "leo"


# 给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，
# 其中 B 中的元素 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。


class Solution:
    def construct_arr(self, a):
        b, tmp = [1] * len(a), 1

        for i in range(1, len(a)):
            b[i] = b[i - 1] * a[i - 1]

        for i in range(len(a) - 2, -1, -1):
            tmp *= a[i + 1]
            b[i] *= tmp

        return b
