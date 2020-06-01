# -*- coding:utf-8 -*-
__author__ = "leo"


# 输入一个整型数组，数组里有正数也有负数。数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。
# 要求时间复杂度为O(n)。


class Solution:
    def max_sub_array(self, nums):
        max_sum = nums[0]
        sum_tmp = nums[0]

        for num in nums[1:]:
            if sum_tmp < 0:
                sum_tmp = num
            else:
                sum_tmp = sum_tmp + num

            if sum_tmp > max_sum:
                max_sum = sum_tmp

        return max_sum
