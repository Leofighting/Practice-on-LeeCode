# -*- coding:utf-8 -*-
__author__ = "leo"

# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
# 你可以假设除了整数 0 之外，这个整数不会以零开头。


class Solution:
    @staticmethod
    def plus_one(digits):
        for i in range(1, len(digits)+1):
            if digits[-i] != 9:
                digits[-i] += 1
                return digits
            digits[-i] = 0
        digits.insert(0, 1)
        return digits


class Solution1:
    @staticmethod
    def plus_one(digits):
        num_str = "".join(str(i) for i in digits)
        num_int = int(num_str) + 1
        res = []
        for i in str(num_int):
            res.append(int(i))
        return res
