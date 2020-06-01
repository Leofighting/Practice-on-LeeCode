# -*- coding:utf-8 -*-
__author__ = "leo"


# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
# 注意：给定 n 是一个正整数。


class Solution:
    def climb_stairs(self, n):
        result = [0, 1, 2]
        for i in range(3, n + 1):
            result.append(result[i - 1] + result[i - 2])
        return result[n]
