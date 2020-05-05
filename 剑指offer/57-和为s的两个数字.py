# -*- coding:utf-8 -*-
__author__ = "leo"


# 输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。
# 如果有多对数字的和等于s，则输出任意一对即可。


class Solution:
    def two_sum(self, nums, target):
        i, j = 0, len(nums) - 1

        while i < j:
            s = nums[i] + nums[j]
            if s > target:
                j -= 1
            elif s < target:
                i += 1
            else:
                return nums[i], nums[j]

        return []
