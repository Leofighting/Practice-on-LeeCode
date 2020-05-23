# -*- coding:utf-8 -*-
__author__ = "leo"


# 输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
# 序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。


class Solution:
    def find_continuous_sequence(self, target):
        if target == 3:
            return [[1, 2]]
        elif target < 5:
            return []

        i = 2
        k = 0
        res = []
        while target >= (i * (i + 1) / 2):
            k += (i - 1)
            if target % i == k % i:
                res.append(list(range((target // i) - (i // 2) + ((i + 1) % 2), (target // i) + (i // 2) + 1)))
            i += 1
        return res[::-1]


