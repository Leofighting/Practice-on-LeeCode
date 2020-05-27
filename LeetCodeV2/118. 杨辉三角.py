# -*- coding:utf-8 -*-
__author__ = "leo"


# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。


class Solution:
    def generate(self, numRows):
        lst = [1] * numRows
        ll = [1] * numRows

        for i in range(numRows):
            old = 1
            for j in range(1, i // 2+1):
                if i >= 2:
                    new = old + lst[j]
                    old = lst[j]
                    lst[j] = new
                    lst[-j-numRows+i] = lst[j]
            ll[i] = lst[:i+1]

        return ll