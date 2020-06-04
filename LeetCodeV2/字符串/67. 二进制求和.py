# -*- coding:utf-8 -*-
__author__ = "leo"


# 给你两个二进制字符串，返回它们的和（用二进制表示）。
# 输入为 非空 字符串且只包含数字 1 和 0。


class Solution:
    def add_binary(self, a, b):
        c = int(a, 2) + int(b, 2)
        return bin(c).replace("0b", "")


class Solution1:
    def add_binary(self, a, b):
        i = len(a) - 1
        j = len(b) - 1
        add = 0
        rel = ""
        while i >= 0 and j >= 0:
            temp = int(a[i]) + int(b[j]) + add
            if temp == 3:
                add = 1
                rel = "1" + rel
            elif temp == 2:
                add = 1
                rel = "0" + rel
            else:
                add = 0
                rel = str(temp) + rel
            i -= 1
            j -= 1

        while i >= 0:
            temp = int(a[i]) + add
            if temp == 3:
                add = 1
