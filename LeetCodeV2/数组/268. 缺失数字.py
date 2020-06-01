# -*- coding:utf-8 -*-
__author__ = "leo"


# 给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。


class Solution:
    def missing_number(self, nums):
        return int(len(nums) * ((1 + len(nums)) / 2) - sum(nums))
