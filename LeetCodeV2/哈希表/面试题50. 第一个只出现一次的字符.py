# -*- coding:utf-8 -*-
__author__ = "leo"


# 在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。


class Solution:
    def first_uniq_char(self, s):
        tmp = set()
        for i, char in enumerate(s, 1):
            if char not in tmp:
                tmp.add(char)
                tmp_string = s[i:]
                if tmp_string.find(char) == -1:
                    return char
        else:
            return " "
