# -*- coding:utf-8 -*-
__author__ = "leo"


# 实现 int sqrt(int x) 函数。
# 计算并返回 x 的平方根，其中 x 是非负整数。
# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。


class Solution:
    def my_sqrt(self, x):
        import math
        return math.floor(math.sqrt(x))


class Solution1:
    def my_sqrt(self, x):
        l, r = 0, x
        while l <= r:
            mid = l + (r - l) // 2
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            elif x < mid * mid:
                r = mid
            else:
                l = mid + 1
