# -*- coding:utf-8 -*-
__author__ = "leo"


# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
# 示例:
# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]


class Solution:
    def move_zero(self, nums):
        if not nums:
            return 0

        j = 0

        for i in range(len(nums)):
            if nums[i]:
                nums[j] = nums[i]
                j += 1

        for i in range(j, len(nums)):
            nums[i] = 0


class Solution1:
    def move_zero(self, nums):
        if not nums:
            return 0

        j = 0

        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
