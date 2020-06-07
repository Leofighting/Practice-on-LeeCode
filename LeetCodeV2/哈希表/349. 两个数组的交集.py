# -*- coding:utf-8 -*-
__author__ = "leo"


# 给定两个数组，编写一个函数来计算它们的交集。
# 示例 1:
# 输入: nums1 = [1,2,2,1], nums2 = [2,2]
# 输出: [2]


class Solution:
    def intersection(self, nums1, nums2):
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        return list(nums1_set & nums2_set)


class Solution1:
    def intersection(self, nums1, nums2):
        s = set(nums1)
        ret = set()

        for i in nums2:
            if i in s:
                ret.add(i)
        return ret
