# -*- coding:utf-8 -*-
__author__ = "leo"


# 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。 


class Solution:
    def min_array(self, numbers):
        if len(numbers) == 1:
            return numbers[0]

        for i in range(len(numbers) - 1):
            if numbers[i] > numbers[i + 1]:
                return numbers[i + 1]
        else:
            return numbers[0]


class Solution1:
    def min_array(self, numbers):
        if not numbers or not len(numbers):
            return -1
        if len(numbers) <= 1:
            return numbers[0]

        left, right = 0, len(numbers) - 1
        while left < right:
            mid = (left + right) // 2
            if numbers[mid] > numbers[right]:
                left = mid + 1
            elif numbers[mid] < numbers[right]:
                right = mid
            else:
                right -= 1
        return numbers[left]
