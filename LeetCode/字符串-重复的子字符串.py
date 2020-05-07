# -*- coding:utf-8 -*-
__author__ = "leo"


# 给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。
# 给定的字符串只含有小写英文字母，并且长度不超过10000。


class Solution:
    def repeated_sub_string_pattern(self, s):
        n = len(s)
        next = [-1] * n

        for i in range(1, n):
            j = next[i - 1]
            while j >= 0 and s[j + 1] != s[i]:
                j = next[j]
            if s[j + 1] == s[i]:
                next[i] = j + 1
        return next[-1] >= 0 and n % (n - 1 - next[-1]) == 0
