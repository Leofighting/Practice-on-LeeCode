# -*- coding:utf-8 -*-
__author__ = "leo"


# 输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
# 序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。


class Solution:
    def find_continuous_sequence(self, target):
        i, j = 1, 1
        sum_ = 0
        res = []

        while i <= target // 2:
            if sum_ < target:
                sum_ += j
                j += 1
            elif sum_ > target:
                sum_ -= i
                i += 1
            else:
                arr = list(range(i, j))
                res.append(arr)

                sum_ -= i
                i += 1
        return res
