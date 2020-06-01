# -*- coding:utf-8 -*-
__author__ = "leo"


# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
# 如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
# 注意：你不能在买入股票前卖出股票。


class Solution:
    def max_profit(self, prices):
        if not prices:
            return 0

        min_ = prices[0]
        res = 0

        for i in prices:
            if i < min_:
                min_ = i
            if i > min_:
                res = max(i - min_, res)

        return res
