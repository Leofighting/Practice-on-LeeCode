# -*- coding:utf-8 -*-
__author__ = "leo"


# 输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。
# 如果有多对数字的和等于s，则输出任意一对即可。


class Solution:
    def two_sum(self, nums, target):
        def find_right(nums, n, l, r, t):
            if l >= r:
                return r

            m = l + (r - l) // 2

            if n + nums[m] == t:
                return m
            elif n + nums[m] < t:
                return find_right(nums, n, m + 1, r, t)
            else:
                return find_right(nums, n, l, m - 1, t)

        def find_left(nums, n, l, r, t):
            if l >= r:
                return l
            m = l + (r - l) // 2

            if n + nums[m] == t:
                return m
            elif n + nums[m] < t:
                return find_left(nums, n, m + 1, r, t)
            else:
                return find_left(nums, n, l, m - 1, t)

        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] + nums[j] == target:
                return [nums[i], nums[j]]
            elif nums[i] + nums[j] > target:
                j = find_right(nums, nums[i], i, j - 1, target)
            elif nums[i] + nums[j] < target:
                i = find_left(nums, nums[j], i + 1, j, target)

        return []
