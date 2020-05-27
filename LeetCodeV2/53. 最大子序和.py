# -*- coding:utf-8 -*-
__author__ = "leo"


# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。


class Solution:
    def max_sub_array(self, nums):
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return nums[0]
        if max(nums) < 0:
            return max(nums)

        for i in range(len(nums)-1):
            if nums[i] > 0:
                nums[i+1] = nums[i+1] + nums[i]

        return max(nums)


class Solution1:
    def max_sub_array(self, nums):
        ans = nums[0]
        summ = 0
        for ele in nums:
            if summ > 0:
                summ += ele
            else:
                summ = ele
            ans = max(ans, summ)
        return ans