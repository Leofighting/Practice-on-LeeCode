# -*- coding:utf-8 -*-
__author__ = "leo"
# 给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    @staticmethod
    def entry_node_of_loop(p_head):
        lst = []
        p = p_head

        while p:
            if p in lst:
                return p
            else:
                lst.append(p)
            p = p.next
