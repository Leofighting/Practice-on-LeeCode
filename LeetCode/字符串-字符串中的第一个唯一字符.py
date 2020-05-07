# -*- coding:utf-8 -*-
__author__ = "leo"

# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。
# 如果不存在，则返回 -1。


from collections import Counter


class Solution:
    def first_uniq_char(self, s):
        count = Counter(s)

        for idx, char in enumerate(s):
            if count[char] == 1:
                return idx

        return -1
