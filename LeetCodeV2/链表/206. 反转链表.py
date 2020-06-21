# -*- coding:utf-8 -*-
__author__ = "leo"


# 反转一个单链表。
# 示例:
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL


class Solution:
    def reverse_list(self, head):
        prev, cur = None, head
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return prev


class Solution1:
    def reverse_list(self, head):
        if head is None:
            return head

        a, b = head, head.next
        a.next = None

        while b:
            c = b.next
            b.next = a
            a, b = b, c

        return a
