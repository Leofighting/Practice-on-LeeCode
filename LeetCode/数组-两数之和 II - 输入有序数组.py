# -*- coding:utf-8 -*-
__author__ = "leo"

# 给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
# 函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。


class Solution:
    @staticmethod
    def two_sum(numbers, target):
        if not numbers:
            return None

        left = 0
        right = len(numbers) - 1
        while left < right:
            _sum = numbers[left] + numbers[right]
            if _sum == target:
                return [left+1, right+1]
            elif _sum > target:
                right -= 1
            else:
                left += 1
        return None


class Solution1:
    @staticmethod
    def two_sum(numbers, target):
        dict_num = {}
        n = len(numbers)
        for i in range(n):
            dict_num[numbers[i]] = i
        for j in range(n):
            tmp = target - numbers[j]
            if (tmp in dict_num) and (j != dict_num[tmp]):
                return [j+1, dict_num[tmp]+1] if j < dict_num[tmp] else [dict_num[tmp]+1, j+1]
        return None
