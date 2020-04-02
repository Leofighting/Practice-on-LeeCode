# -*- coding:utf-8 -*-
__author__ = "leo"

# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。


class Solution:
    @staticmethod
    def max_sub_array(nums):
        tmp = nums[0]
        max_ = tmp
        n = len(nums)
        for i in range(1, n):
            if tmp + nums[i] > nums[i]:
                max_ = max(max_, tmp+nums[i])
                tmp = tmp + nums[i]
            else:
                max_ = max(max_, tmp, tmp+nums[i], nums[i])
                tmp = nums[i]
        return max_
