# -*- coding:utf-8 -*-
__author__ = "leo"


# 给定两个数组，编写一个函数来计算它们的交集。
# 示例 1:
# 输入: nums1 = [1,2,2,1], nums2 = [2,2]
# 输出: [2,2]


class Solution:
    def intersect(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        r = []
        left, right = 0, 0

        while left < len(nums1) and right < len(nums2):
            if nums1[left] < nums2[right]:
                left += 1
            elif nums1[left] == nums2[right]:
                r.append(nums1[left])
                left += 1
                right += 1
            else:
                right += 1

        return r
