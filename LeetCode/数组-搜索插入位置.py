# -*- coding:utf-8 -*-
__author__ = "leo"

# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
# 如果目标值不存在于数组中，返回它将会被按顺序插入的位置。


class Solution:
    @staticmethod
    def search_insert(nums, target):
        if not nums:
            return 0
        n = len(nums)
        left = 0
        right = n-1
        res = -1
        while left <= right:
            mid = (left+right) //2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        res = left
        return res
