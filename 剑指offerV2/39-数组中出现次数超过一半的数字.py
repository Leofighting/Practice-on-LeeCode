# -*- coding:utf-8 -*-
__author__ = "leo"


# 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。


class Solution:
    def majority_element(self, nums):
        nums = sorted(nums)
        return nums[int(len(nums) / 2)]
