# -*- coding:utf-8 -*-
__author__ = "leo"


# 定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverse_list(self, head):
        pre = None
        cur = head

        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp

        return pre
