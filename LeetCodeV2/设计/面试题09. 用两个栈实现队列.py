# -*- coding:utf-8 -*-
__author__ = "leo"


# 用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )


class CQueue:
    def __init__(self):
        self.res = []

    def appendTail(self, value):
        self.res.append(value)

    def deleteHead(self):
        if not self.res:
            return -1
        return self.res.pop(0)