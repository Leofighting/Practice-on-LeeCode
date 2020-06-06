# -*- coding:utf-8 -*-
__author__ = "leo"


# 编写一个方法，找出两个数字a和b中最大的那一个。不得使用if-else或其他比较运算符。


class Solution:
    def maximum(self, a, b):
        return int(((a + b) + abs(a - b)) / 2)


class Solution1:
    def maximum(self, a, b):
        return sorted([a, b])[1]
