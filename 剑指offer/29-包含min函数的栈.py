# -*- coding:utf-8 -*-
__author__ = "leo"


# 定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，
# 调用 min、push 及 pop 的时间复杂度都是 O(1)。


class Solution:
    def __init__(self):
        self.A, self.B = [], []

    def push(self, x):
        self.A.append(x)
        if not self.B or self.B[-1] >= x:
            self.B.append(x)

    def pop(self):
        if self.A.pop() == self.B[-1]:
            self.B.pop()

    def top(self):
        return self.A[-1]

    def min(self):
        return self.B[-1]
