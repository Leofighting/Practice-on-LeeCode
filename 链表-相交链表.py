# -*- coding:utf-8 -*-
__author__ = "leo"

# 编写一个程序，找到两个单链表相交的起始节点。


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def get_intersection_Node(self, headA, headB):
        ha, hb = headA, headB

        while ha != hb:
            ha = ha.next if ha else headB
            hb = hb.next if hb else headA

        return ha
