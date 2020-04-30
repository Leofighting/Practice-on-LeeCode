# -*- coding:utf-8 -*-
__author__ = "leo"


# 输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def merge_two_lists(self, l1, l2):
        cur = dum = ListNode(0)

        while l1 and l2:
            if l1.val < l2.val:
                cur.next, l1 = l1, l1.next
            else:
                cur.next, l2 = l2, l2.next
            cur = cur.next

        cur.next = l1 if l1 else l2

        return dum.next
