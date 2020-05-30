# -*- coding:utf-8 -*-
__author__ = "leo"


# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。


class Solution:
    def rotate(self, nums, k):
        nums[:] = nums[len(nums) - k:] + nums[:len(nums) - k]


class Solution1:
    def rotate(self, nums, k):
        n = len(nums)
        k %= n
        nums[:] = nums[-k:] + nums[:-k]
