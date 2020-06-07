# -*- coding:utf-8 -*-
__author__ = "leo"


# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
# 示例 1:
# 输入: s = "anagram", t = "nagaram"
# 输出: true


class Solution:
    def is_anagram(self, s, t):
        s_set = set(s)
        t_set = set(t)
        if s_set == t_set:
            for i in s_set:
                if s.count(i) != t.count(i):
                    return False
            return True
        else:
            return False
