# -*- coding:utf-8 -*-
__author__ = "leo"

# 编写一个程序，找到两个单链表相交的起始节点。


class Solution:
    def get_intersection_node(self, headA, headB):
        if not headA or not headB:
            return None

        cur_a = headA
        cur_b = headB

        while (cur_a is not None) or (cur_b is not None):
            if cur_a == cur_b:
                return cur_a
            else:
                if cur_a is None:
                    cur_a = headB
                else:
                    cur_a = cur_a.next
                if cur_b is None:
                    cur_b = headA
                else:
                    cur_b = cur_b.next

        return None


class Solution1:
    def get_intersection_node(self, headA, headB):
        all_a = set()
        while headA:
            all_a.add(headA)
            headA = headA.next
        while headB and headB not in all_a:
            headB = headB.next

        return headB if headB is not None else None
