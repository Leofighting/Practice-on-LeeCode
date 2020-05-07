# -*- coding:utf-8 -*-
__author__ = "leo"


# 给定两个没有重复元素的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。找到 nums1 中每个元素在 nums2 中的下一个比其大的值。
# nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出-1。


class Solution:
    def next_greater_element(self, nums1, nums2):
        stack, hash_map = list(), dict()

        for i in nums2:
            while len(stack) != 0 and stack[-1] < i:
                hash_map[stack.pop()] = i
            stack.append(i)
        return [hash_map.get(i, -1) for i in nums1]


class Solution1:
    def next_greater_element(self, nums1, nums2):
        ans = []
        for n1 in nums1:
            temp = -1
            for n2 in nums2[nums2.index(n1):]:
                if n2 > n1:
                    temp = n2
                    break
            ans.append(temp)
        return ans
