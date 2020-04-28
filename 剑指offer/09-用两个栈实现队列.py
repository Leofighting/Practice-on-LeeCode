# -*- coding:utf-8 -*-
__author__ = "leo"

# 用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )


class Solution:
    def __init__(self):
        self.in_stack, self.out_stack = [], []

    def append_tail(self, value):
        self.in_stack.append(value)

    def delete_head(self):
        if self.out_stack:
            return self.out_stack.pop()
        if not self.in_stack:
            return -1
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()
