# -*- coding:utf-8 -*-
__author__ = "leo"


class Solution:
    def roman_to_int(self, s):
        dic = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
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
