# -*- coding:utf-8 -*-
__author__ = "leo"


# 找出数组中重复的数字。
# 在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。
# 数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。


class Solution:
    def find_repeat_number(self, nums):
        count = set()
        for i in nums:
            if i in count:
                return i
            else:
                count.add(i)
