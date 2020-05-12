# -*- coding:utf-8 -*-
__author__ = "leo"


# 写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项。斐波那契数列的定义如下：
# F(0) = 0,   F(1) = 1
# F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
# 斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。
# 答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。


class Solution:
    def fib(self, n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b

        return a % 1000000007


class Solution1:
    def fib(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        memo = [i for i in range(n + 1)]
        memo[0], memo[1] = 0, 1
        for i in range(2, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2]

        return memo[n] % 1000000007
