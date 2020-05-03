# -*- coding:utf-8 -*-
__author__ = "leo"


# 输入一个整型数组，数组里有正数也有负数。
# 数组中的一个或连续多个整数组成一个子数组。
# 求所有子数组的和的最大值。

class Solution:
    def max_subarray(self, nums):
        for i in range(1, len(nums)):
            nums[i] += max(nums[i - 1], 0)
        return max(nums)
