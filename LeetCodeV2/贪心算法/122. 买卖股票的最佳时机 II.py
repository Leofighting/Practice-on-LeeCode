# -*- coding:utf-8 -*-
__author__ = "leo"


# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
# 设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。


class Solution:
    def max_profit(self, prices):
        if not len(prices):
            return 0
        mi = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] >= prices[i - 1]:
                continue
            profit += prices[i - 1] - mi
            mi = prices[i]

        profit += prices[-1] - mi
        return profit


class Solution1:
    def max_profit(self, prices):
        profit = 0
        lens = len(prices)

        for i in range(1, lens):
            j = prices[i] - prices[i - 1]
            if j > 0:
                profit += j

        return profit
