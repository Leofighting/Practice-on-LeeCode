# -*- coding:utf-8 -*-
__author__ = "leo"

# 用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，
# 分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )


class CQueue:
    def __init__(self):
        self.queue = []

    def append_tail(self, value):
        self.queue.append(value)

    def delete_head(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        else:
            return -1


class CQueue1:
    def __init__(self):
        self.a, self.b = [], []

    def append_tail(self, value):
        self.a.append(value)

    def delete_head(self):
        if self.b:
            return self.b.pop()
        if not self.a:
            return -1
        while self.a:
            self.b.append(self.a.pop())
        return self.b.pop()
