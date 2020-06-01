# -*- coding:utf-8 -*-
__author__ = "leo"


# 给定一个非空数组，返回此数组中第三大的数。如果不存在，则返回数组中最大的数。要求算法时间复杂度必须是O(n)。


class Solution:
    def third_max(self, nums):
        nums_set = set(nums)
        nums_non_repeat = list(nums_set)
        nums_non_repeat.sort()
        if len(nums_non_repeat) > 2:
            return nums_non_repeat[-3]
        else:
            return nums_non_repeat[-1]
