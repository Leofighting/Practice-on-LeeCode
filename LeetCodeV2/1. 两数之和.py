# -*- coding:utf-8 -*-
__author__ = "leo"


# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。


class Solution:
    def two_sum(self, nums, target):
        d = {}
        for i, num in enumerate(nums):
            if target - num in d:
                return [d.get(target-num), i]
            d[num] = i

        return []