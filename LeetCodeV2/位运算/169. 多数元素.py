# -*- coding:utf-8 -*-
__author__ = "leo"


class Solution:
    def majority_element(self, nums):
        from collections import Counter
        n = len(nums)
        counter = Counter(nums)
        for k, v in counter.items():
            if v > n / 2:
                return k


class Solution1:
    def majority_element(self, nums):
        nums.sort()
        return nums[len(nums) // 2]
