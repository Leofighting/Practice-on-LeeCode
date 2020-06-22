# -*- coding:utf-8 -*-
__author__ = "leo"


# 给定一个带有头结点 head 的非空单链表，返回链表的中间结点。
# 如果有两个中间结点，则返回第二个中间结点。


class Solution:
    def middle_node(self, head):
        if not head or not head.next:
            return head

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


class Solution1:
    def middle_node(self, head):
        if not head:
            return 0
        n = 0
        head_c = head

        while head_c:
            n += 1
            head_c = head_c.next

        head_c = head

        for i in range((n - 1) // 2):
            head_c = head_c.next

        if n % 2 == 0:
            return head_c.next
        else:
            return head_c
