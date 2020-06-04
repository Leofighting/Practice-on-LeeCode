# -*- coding:utf-8 -*-
__author__ = "leo"


# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。


class Solution:
    def reverse(self, x):
        negative_flag = 1
        if x < 0:
            x = abs(x)
            negative_flag = -1
        res = tmp = 0

        while x:
            tmp = x % 10
            x = x // 10
            res = res * 10 + tmp

        result = negative_flag * res

        return result if -2 ** 31 < result < 2 ** 31 - 1 else 0
