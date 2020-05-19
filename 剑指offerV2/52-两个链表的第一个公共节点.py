# -*- coding:utf-8 -*-
__author__ = "leo"


class Solution:
    def get_intersection_node(self, head_a, head_b):
        p1 = head_a
        p2 = head_b

        while p1 != p2:
            if not p1:
                p1 = head_b
            else:
                p1 = p1.next

            if not p2:
                p2 = head_a
            else:
                p2 = p2.next

        return p1


class Solution1:
    def get_intersection_node(self, head_a, head_b):
        visited_set = set()

        while head_a:
            visited_set.add(head_a)
            head_a = head_a.next

        while head_b:
            if head_b in visited_set:
                return head_b
            head_b = head_b.next
        return None