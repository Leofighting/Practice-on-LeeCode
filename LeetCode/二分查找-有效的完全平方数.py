# -*- coding:utf-8 -*-
__author__ = "leo"


# 给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。
# 说明：不要使用任何内置的库函数，如  sqrt。
# 示例 1：
# 输入：16
# 输出：True


class Solution:
    def is_perfect_square(self, num):
        i = 1

        while i * i < num:
            i += 1

        return i * i == num


class Solution1:
    def is_perfect_square(self, num):
        left, right = 1, num

        while left < right:
            mid = (left + right) // 2
            if mid * mid < num:
                left = mid + 1
            else:
                right = mid

        return left * left == num


class Solution2:
    def is_perfect_square(self, num):
        i = 1
        while num > 0:
            num -= i
            i += 2
        return num == 0
