# -*- coding:utf-8 -*-
__author__ = "leo"


# 给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。
# 返回删除后的链表的头节点。


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def delete_node(self, head, val):
        if head.val == val:
            return head.next

        pre, cur = head, head.next

        while cur and cur.val != val:
            pre, cur = cur, cur.next

        if cur:
            pre.next = cur.next

        return head
