# -*- coding:utf-8 -*-
__author__ = "leo"

# 给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，
# 找出 0 .. n 中没有出现在序列中的那个数。


class Solution:
    def missing_number(self, nums):
        nums.sort()

        if nums[-1] != len(nums):
            return len(nums)

        elif nums[0] != 0:
            return 0

        for i in range(1, len(nums)):
            expect_num = nums[i-1] + 1
            if nums[i] != expect_num:
                return expect_num


class Solution1:
    def missing_number(self, nums):
        num_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number
