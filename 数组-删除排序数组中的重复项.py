# -*- coding:utf-8 -*-
__author__ = "leo"

# 给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
# 不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。


class Solution:
    @staticmethod
    def remove_duplicates(nums):
        flag = 0
        if not nums:
            return flag

        for i in range(1, len(nums)):
            if nums[i] != nums[flag]:
                flag += 1
                nums[flag] = nums[i]
        return flag + 1


class Solution1:
    @staticmethod
    def remove_duplicates(nums):
        if not nums:
            return 0
        i = 1

        while i <= len(nums) - 1:
            if nums[i] == nums[i-1]:
                del nums[i]
            else:
                i += 1

        return len(nums)
