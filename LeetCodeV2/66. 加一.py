# -*- coding:utf-8 -*-
__author__ = "leo"


# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
# 你可以假设除了整数 0 之外，这个整数不会以零开头。


class Solution:
    def plus_one(self, digits):
        n = len(digits)
        i = n - 1
        while i >= 0:
            if digits[i] != 9:
                digits[i] += 1
                return digits
            digits[i] = 0
            i -= 1
        digits.insert(0, 1)
        return digits


class Solution1:
    def plus_one(self, digits):
        idx = len(digits) - 1
        while idx >= 0:
            digits[idx] += 1
            digits[idx] %= 10
            if digits[idx] != 0:
                return digits
            idx -= 1
        res = [0] * (len(digits) + 1)
        res[0] = 1
        return res
