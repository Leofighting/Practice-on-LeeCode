# -*- coding:utf-8 -*-
__author__ = "leo"


# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。


class Solution:
    def is_palindrome(self, x):
        x = str(x)
        y = x[::-1]
        return x == y


class Solution1:
    def is_palindrome(self, x):
        a = str(x)
        b = int(len(a) / 2)
        i = 0

        while b - i:
            if a[i] == a[-1 - i]:
                i += 1
                continue
            else:
                return False

        return True
