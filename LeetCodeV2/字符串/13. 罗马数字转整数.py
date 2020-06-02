# -*- coding:utf-8 -*-
__author__ = "leo"


# 罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。
#
# 字符          数值
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000


class Solution:
    def roman_to_int(self, s):
        dic = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        num = 0
        num_2 = 0
        for i in reversed(s):
            d = dic.get(i)
            if d < num:
                num_2 -= d
            else:
                num_2 += d
                num = d
        return num_2


class Solution1:
    def roman_to_int(self, s):
        dic = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        sum_ = 0
        pre = 0
        for i in s:
            cur = dic.get(i)
            sum_ += cur - pre * 2 if pre < cur else cur
            pre = cur
        return sum_
