# -*- coding:utf-8 -*-
__author__ = "leo"


# 给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。
#
# 说明：不要使用任何内置的库函数，如  sqrt。


class Solution:
    def is_perfect_square(self, num):
        left = 1
        right = num // 2

        while left < right:
            m = (left + right) // 2
            if m * m < num:
                left = m + 1
            else:
                right = m

        return left * left == num
