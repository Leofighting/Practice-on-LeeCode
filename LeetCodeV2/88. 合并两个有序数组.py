# -*- coding:utf-8 -*-
__author__ = "leo"


# 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。


class Solution:
    def merge(self, nums1, m, nums2, n):
        if n == 0:
            return None
        if len(nums1) == n:
            nums1[:] = nums2[:]
            return None

        cur = m + n - 1
        p1, p2 = m - 1, n - 1

        while True:
            if nums1[p1] > nums2[p2]:
                nums1[cur] = nums1[p1]
                p1 -= 1
            else:
                nums1[cur] = nums2[p2]
                p2 -= 1
            cur -= 1
            if p1 < 0:
                nums1[:cur + 1] = nums2[:p2 + 1]
                return
            if p2 < 0:
                return
