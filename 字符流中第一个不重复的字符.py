# -*- coding:utf-8 -*-
__author__ = "leo"

# 请实现一个函数用来找出字符流中第一个只出现一次的字符。
# 例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。
# 当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。


class Solution:
    def __init__(self):
        self.s = ""
        self.dict1 = {}

    def first_appearing_once(self):
        for i in self.s:
            if self.dict1[i] == 1:
                return i
        return "#"

    def insert(self, char):
        self.s += char
        if char in self.dict1:
            self.dict1[char] += 1
        else:
            self.dict1[char] = 1
