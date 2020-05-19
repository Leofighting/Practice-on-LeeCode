# -*- coding:utf-8 -*-
__author__ = "leo"


# 统计一个数字在排序数组中出现的次数。


class Solution:
    def search(self, nums, target):
        n = len(nums)
        if not n:
            return 0

        l, r = 0, n

        while l < r:
            m = (l + r) // 2
            if nums[m] <= target:
                l = m + 1
            else:
                r = m

        if l == n and nums[-1] != target:
            return 0

        br = l
        l, r = 0, n

        while l < r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m

        return br - l


class Solution1:
    def search(self, nums, target):
        from collections import Counter
        obj = Counter(nums)
        return obj[target]
