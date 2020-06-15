# -*- coding:utf-8 -*-
__author__ = "leo"

# 给出由小写字母组成的字符串 S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。
# 在 S 上反复执行重复项删除操作，直到无法继续删除。
# 在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。
from string import ascii_lowercase


class Solution:
    def remove_duplicates(self, s):
        duplicates = {2 * ch for ch in ascii_lowercase}

        prev_length = -1

        while prev_length != len(s):
            prev_length = len(s)
            for d in duplicates:
                s = s.replace(d, "")

        return s
