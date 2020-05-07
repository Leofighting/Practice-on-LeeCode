# -*- coding:utf-8 -*-
__author__ = "leo"

# 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。

from collections import Counter


class Solution:
    def majority_element(self, nums):
        counts = Counter(nums)
        return max(counts.keys(), key=counts.get)


class Solution1:
    def majority_element(self, nums):
        nums.sort()
        return nums[len(nums) // 2]