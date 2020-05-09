# -*- coding:utf-8 -*-
__author__ = "leo"

# 请实现一个函数，把字符串 s 中的每个空格替换成"%20"。


class Solution:
    def replace_space(self, s):
        res = []
        for char in s:
            if char == " ":
                res.append("%20")
            else:
                res.append(char)
        return "".join(res)


class Solution1:
    def replace_space(self, s):
        return s.replace(" ", "%20")


class Solution2:
    def replace_space(self, s):
        s = list(s)

        for i in range(len(s)):
            if s[i] == " ":
                s[i] = "%20"

        return "".join(s)
