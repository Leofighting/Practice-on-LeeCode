# -*- coding:utf-8 -*-
__author__ = "leo"

# 给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
# 不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。


class Solution:
    @staticmethod
    def remove_element(nums, val):
        if not nums:
            return 0
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i


class Solution1:
    @staticmethod
    def remove_element(nums, val):
        j = nums.index(val) if val in nums else len(nums)
        for i in range(j+1, len(nums)):
            if nums[i] != val:
                nums[i] = nums[j]
                j += 1
        return j
