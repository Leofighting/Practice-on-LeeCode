# -*- coding:utf-8 -*-
__author__ = "leo"


# 给定一个链表，判断链表中是否有环。
# 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
# 如果 pos 是 -1，则在该链表中没有环。


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def has_cycle(self, head):
        if not head:
            return False

        target = {head}
        head = head.next

        while head:
            if head in target:
                return True
            else:
                target.add(head)
                head = head.next
        return False


class Solution1:
    def has_cycle(self, head):
        if not head:
            return False

        p, q = head, head

        while q:
            if not q.next:
                return False
            else:
                p = p.next
                q = q.next.next

            if p == q:
                return True

        return False
