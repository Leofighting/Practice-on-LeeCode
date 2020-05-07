# -*- coding:utf-8 -*-
__author__ = "leo"


# 请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点，你将只被给定要求被删除的节点。


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def delete_node(self, node):
        node.val = node.next.val
        node.next = node.next.next
