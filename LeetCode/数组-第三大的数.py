# -*- coding:utf-8 -*-
__author__ = "leo"

# 给定一个非空数组，返回此数组中第三大的数。如果不存在，则返回数组中最大的数。要求算法时间复杂度必须是O(n)

import math


class Solution:
    def third_max(self, nums):
        r = [float("-inf"), float("-inf"), float("-inf")]

        for n in nums:
            if n in r:
                continue

            if n > r[0]:
                r = [n, r[0], r[1]]

            elif n > r[1]:
                r = [r[0], n, r[1]]

            elif n > r[2]:
                r[2] = n

        return r[0] if math.isinf(r[2]) else r[2]
