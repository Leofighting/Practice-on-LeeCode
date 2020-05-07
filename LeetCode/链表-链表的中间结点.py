# -*- coding:utf-8 -*-
__author__ = "leo"


# 给定一个带有头结点 head 的非空单链表，返回链表的中间结点。
# 如果有两个中间结点，则返回第二个中间结点。


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def middle_node(self, head):
        if head is None:
            return None

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
