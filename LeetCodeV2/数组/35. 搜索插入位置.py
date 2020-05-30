# -*- coding:utf-8 -*-
__author__ = "leo"


# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 你可以假设数组中无重复元素。


class Solution:
    def search_insert(self, nums, target):
        left, right = 0, len(nums) - 1

        if nums[right] < target:
            return len(nums)

        while left <= right:
            mid = int((left + right) / 2)
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid

        return left
