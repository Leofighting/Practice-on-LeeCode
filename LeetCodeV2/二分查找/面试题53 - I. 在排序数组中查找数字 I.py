# -*- coding:utf-8 -*-
__author__ = "leo"


# 统计一个数字在排序数组中出现的次数。


class Solution:
    def search(self, nums, target):
        len_nums = len(nums)
        if len_nums == 0:
            return 0
        elif len_nums == 1:
            if nums[0] == target:
                return 1
            else:
                return 0
        else:
            return nums.count(target)
