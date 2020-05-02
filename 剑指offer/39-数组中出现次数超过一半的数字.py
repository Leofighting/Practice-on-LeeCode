# -*- coding:utf-8 -*-
__author__ = "leo"

# 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。


from collections import Counter


class Solution:
    def majority_element(self, nums):
        votes = 0
        for num in nums:
            if votes == 0:
                x = num
            votes += 1 if num == x else -1
        return x


class Solution1:
    def majority_element(self, nums):
        obj = Counter(nums)
        length = len(nums)
        for k, v in obj.items():
            if v > length // 2:
                return k
