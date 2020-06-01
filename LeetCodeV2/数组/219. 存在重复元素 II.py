# -*- coding:utf-8 -*-
__author__ = "leo"


# 给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的 绝对值 至多为 k。


class Solution:
    def contains_nearby_duplicate(self, nums, k):
        dic = {}
        if len(nums) == len(set(nums)):
            return False

        for i, char in enumerate(nums):
            if char in dic and i - dic[char] <= k:
                return True
            dic[char] = i

        return False
