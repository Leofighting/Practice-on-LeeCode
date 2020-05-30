# -*- coding:utf-8 -*-
__author__ = "leo"


# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。


class Solution:
    def move_zeroes(self, nums):
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

        return nums


class Solution1:
    def move_zeroes(self, nums):
        n = len(nums)

        while n > 0:
            n -= 1
            if nums[n] == 0:
                nums.pop(n)
                nums.append(0)
