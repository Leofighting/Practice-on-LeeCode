# -*- coding:utf-8 -*-
__author__ = "leo"


# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。


class Solution:
    def reverse_force(self, x):
        res = 0
        news = abs(x)
        while news != 0:
            temp = news % 10
            res = res * 10 + temp
            news //= 10

        if x < 0:
            if -res >= -2 ** 31:
                return -res
            else:
                return 0
        else:
            if res <= 2 ** 31 - 1:
                return res
            else:
                return 0
