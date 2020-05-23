# -*- coding:utf-8 -*-
__author__ = "leo"


# 输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。为简单起见，标点符号和普通字母一样处理。
# 例如输入字符串"I am a student. "，则输出"student. a am I"。


class Solution:
    def reverse_words(self, s):
        seperate = s.split()
        ans = ""
        for i in seperate:
            ans = " " + i + ans

        return ans[1:]


class Solution1:
    def reverse_words(self, s):
        s = s.strip()
        a = s.split()
        a = a[::-1]
        return " ".join(a)

