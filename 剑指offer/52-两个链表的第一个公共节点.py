# -*- coding:utf-8 -*-
__author__ = "leo"


# 输入两个链表，找出它们的第一个公共节点。


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def get_intersection_node(self, headA, headB):
        node1, node2 = headA, headB

        while node1 != node2:
            node1 = node1.next if node1 else headB
            node2 = node2.next if node2 else headA

        return node1
