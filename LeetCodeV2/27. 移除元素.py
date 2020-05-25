# -*- coding:utf-8 -*-
__author__ = "leo"


# 给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
# 不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
# 元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。


class Solution:
    def remove_element(self, nums, val):
        p, q = 0, 0
        n = len(nums)
        while q < n:
            if nums[q] != val:
                nums[q], nums[p] = nums[p], nums[q]
                p += 1
            q += 1
        return p


class Solution1:
    def remove_element(self, nums, val):
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
        return len(nums)
