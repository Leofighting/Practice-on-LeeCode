# -*- coding:utf-8 -*-
__author__ = "leo"


# 字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。
# 比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。


class Solution:
    def reverse_left_words(self, s, n):
        return s[n:] + s[:n]


class Solution1:
    def reverse_left_words(self, s, n):
        res = []
        for i in range(n, len(s)):
            res.append(s[i])
        for i in range(n):
            res.append(s[i])

        return "".join(res)


class Solution2:
    def reverse_left_words(self, s, n):
        res = []
        for i in range(n, n + len(s)):
            res.append(s[i % len(s)])
        return "".join(res)

