# -*- coding:utf-8 -*-
__author__ = "leo"

# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。


class Solution:
    @staticmethod
    def two_sum(nums, target):
        lens = len(nums)
        j = -1
        for i in range(1, lens):
            temp = nums[:i]
            if (target - nums[i]) in temp:
                j = temp.index(target - nums[i])
                break

        if j >= 0:
            return [j, i]


class Solution1:
    @staticmethod
    def two_sum(nums, target):
        hash_map = {}
        for i, num in enumerate(nums):
            if target - num in hash_map:
                return [i, hash_map[target - num]]
            hash_map[num] = i


