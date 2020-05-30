# -*- coding:utf-8 -*-
__author__ = "leo"


# 给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

# 函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。


class Solution:
    def two_sum(self, numbers, target):
        i = 0
        j = len(numbers) - 1
        while numbers[i] + numbers[j] != target:
            if numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] < target:
                i += 1

        return [i + 1, j + 1]
