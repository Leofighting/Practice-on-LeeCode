# -*- coding:utf-8 -*-
__author__ = "leo"


# 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。


class Solution:
    def majority_element(self, nums):
        from collections import Counter
        n = len(nums)
        counter = Counter(nums)
        for k, v in counter.items():
            if v > n / 2:
                return k
