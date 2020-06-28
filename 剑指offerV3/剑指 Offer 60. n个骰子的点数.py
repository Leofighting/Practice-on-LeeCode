# -*- coding:utf-8 -*-
__author__ = "leo"


# 把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。


class Solution:
    def two_sum(self, n):
        if n == 0:
            return []

        cnts = [0] + [1] * 6 + [0] * (6 * n - 6)
        for _ in range(n - 1):
            for i in range(6 * n, 0, -1):
                cnts[i] = sum(cnts[max(i - 6, 0): i])

        return filter(lambda a: a != 0, list(map(lambda a: a / 6 ** n, cnts)))
