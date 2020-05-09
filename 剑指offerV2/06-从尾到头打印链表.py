# -*- coding:utf-8 -*-
__author__ = "leo"

# 输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverse_print(self, head):
        return self.reverse_print(head.next) + [head.val] if head else []


class Solution1:
    def reverse_print(self, head):
        stack = []
        while head:
            stack.append(head.val)
            head = head.next

        return stack[::-1]


class Solution2:
    def reverse_print(self, head):
        res = []
        p = head

        def helper(p):
            if not p:
                return None
            helper(p.next)
            res.append(p.val)

        helper(p)
        return res
