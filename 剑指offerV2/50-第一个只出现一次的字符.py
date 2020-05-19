# -*- coding:utf-8 -*-
__author__ = "leo"

# 在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。


class Solution:
    def first_uniq_char(self, s):
        c = list()
        visited = set()

        for i in s:
            if i not in visited:
                if i in c:
                    visited.add(i)
                    del c[c.index(i)]
                else:
                    c.append(i)

        if len(c) == 0:
            return " "
        return c[0]