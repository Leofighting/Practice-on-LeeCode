# -*- coding:utf-8 -*-
__author__ = "leo"


# 统计一个数字在排序数组中出现的次数。


class Solution:
    def search(self, nums, target):
        i, j = 0, len(nums) - 1

        while i <= j:
            m = (i + j) // 2
            if nums[m] <= target:
                i = m + 1
            else:
                j = m - 1
        right = i

        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] < target:
                i = m + 1
            else:
                j = m - 1
        left = j

        return right - left - 1
