# -*- coding:utf-8 -*-
__author__ = "leo"


# 给你两个有序整数数组 nums1 和 nums2
# 请你将 nums2 合并到 nums1 中，使 num1 成为一个有序数组。


class Solution1:
    # 方法一 : 合并后排序
    @staticmethod
    def merge(nums1, m, nums2, n):
        nums1[:] = sorted(nums1[:m] + nums2)


class Solution2:
    # 方法二 : 双指针 / 从前往后
    @staticmethod
    def merge(nums1, m, nums2, n):
        nums1_copy = nums1[:m]
        nums1[:] = []

        p1, p2 = 0, 0

        while p1 < m and p2 < n:
            if nums1_copy[p1] < nums2[p2]:
                nums1.append(nums1_copy[p1])
                p1 += 1
            else:
                nums1.append(nums2[p2])
                p2 += 1

        if p1 < m:
            nums1[p1 + p2:] = nums1_copy[p1:]
        if p2 < n:
            nums1[p1 + p2:] = nums2[p2:]


class Solution3:
    # 方法三 : 双指针 / 从后往前
    @staticmethod
    def merge(nums1, m, nums2, n):
        p1, p2, p = m - 1, n - 1, m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1

        nums1[:p2 + 1] = nums2[:p2 + 1]
