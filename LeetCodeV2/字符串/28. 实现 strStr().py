# -*- coding:utf-8 -*-
__author__ = "leo"

# 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。


class Solution:
    def str_str(self, haystack, needle):
        m, n = len(haystack), len(needle)
        if n == 0:
            return 0
        elif n > m:
            return -1
        for i in range(m-n+1):
            if haystack[i] == needle[0]:
                if haystack[i:i+n] == needle:
                    return i
                else:
                    continue
        return -1


class Solution1:
    def str_str(self, haystack, needle):
        try:
            return haystack.index(needle)
        except ValueError:
            return -1


class Solution2:
    def str_str(self, haystack, needle):
        if needle in haystack:
            return haystack.find(needle)
        else:
            return -1