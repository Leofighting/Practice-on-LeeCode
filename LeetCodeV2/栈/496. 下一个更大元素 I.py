# -*- coding:utf-8 -*-
__author__ = "leo"

# 给定两个 没有重复元素 的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。找到 nums1 中每个元素在 nums2 中的下一个比其大的值。
# nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出 -1 。


class Solution:
    def next_great_element(self, nums1, nums2):
        stack = []
        mp = {}

        for x in nums2:
            if not stack or stack[-1] >= x:
                stack.append(x)
            else:
                while stack and stack[-1] < x:
                    mp[stack.pop()] = x
                stack.append(x)

        return [mp.get(x, -1) for x in nums1]
