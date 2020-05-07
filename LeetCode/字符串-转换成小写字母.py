# -*- coding:utf-8 -*-
__author__ = "leo"

# 实现函数 ToLowerCase()，该函数接收一个字符串参数 str，并将该字符串中的大写字母转换成小写字母，之后返回新的字符串。

class Solution:
    def to_lower_case(self, s):
        result = ""
        for i in s:
            if "A" <= i <= "Z":
                i = chr(ord(i) + 32)
            else:
                pass

            result += i

        return result
