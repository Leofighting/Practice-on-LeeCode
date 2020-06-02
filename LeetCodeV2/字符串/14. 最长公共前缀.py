# -*- coding:utf-8 -*-
__author__ = "leo"


# 编写一个函数来查找字符串数组中的最长公共前缀。
# 如果不存在公共前缀，返回空字符串 ""。


class Solution:
    def longest_common_prefix(self, strs):
        res = ""
        for i in zip(*strs):
            if len(set(i)) == 1:
                res += i[0]
            else:
                break
        return res
