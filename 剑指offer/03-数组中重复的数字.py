# -*- coding:utf-8 -*-
__author__ = "leo"

# 找出数组中重复的数字。
# 在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。
# 示例 1：
# 输入：
# [2, 3, 1, 0, 2, 5, 3]
# 输出：2 或 3


from collections import Counter


class Solution:
    def find_repeat_number(self, nums):
        count = Counter(nums)
        for key, value in count.items():
            if value > 1:
                return key
        return None


class Solution1:
    def find_repeat_number(self, nums):
        nums.sort()
        pre = nums[0]

        for index in range(1, len(nums)):
            if pre == nums[index]:
                return pre
            pre = nums[index]


class Solution2:
    def find_repeat_number(self, nums):
        dic = dict()
        for i in nums:
            if i not in dic:
                dic[i] = 0
            else:
                return i

