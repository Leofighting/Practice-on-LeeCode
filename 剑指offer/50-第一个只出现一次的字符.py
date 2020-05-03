# -*- coding:utf-8 -*-
__author__ = "leo"


# 在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格

class Solution:
    def first_uniq_char(self, s):
        dic = {}
        for c in s:
            dic[c] = not (c in dic)
        for c in s:
            if dic[c]:
                return c
        return " "


class Solution1:
    def first_uniq_char(self, s):
        from collections import OrderedDict
        dic = OrderedDict()
        for c in s:
            dic[c] = not (c in dic)
        for k, v in dic.items():
            if v:
                return k
        return " "

