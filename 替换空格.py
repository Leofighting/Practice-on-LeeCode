# -*- coding:utf-8 -*-
__author__ = "leo"

# 请实现一个函数，将一个字符串中的每个空格替换成“%20”。
# 例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。


class Solution:
    @staticmethod
    def replace_space(s):
        return s.replace(" ", "%20")


class Solution1:
    @staticmethod
    def replace_space(s):
        s_list = list(s)
        count = len(s_list)

        for i in range(count):
            if s_list[i] == " ":
                s_list[i] = "%20"

        return "".join(s_list)