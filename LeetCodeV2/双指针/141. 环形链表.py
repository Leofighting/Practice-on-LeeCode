# -*- coding:utf-8 -*-
__author__ = "leo"


# 给定一个链表，判断链表中是否有环。
# 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。


class Solution:
    def has_cycle(self, head):
        check = set()

        while head:
            if head in check:
                return True
            else:
                check.add(head)
            head = head.next

        return False


class Solution1:
    def has_cycle(self, head):
        slow = fast = head
        while True:
            if fast is None:
                return False
            slow = slow.next
            fast = fast.next and fast.next.next
            if slow == fast and slow is not None:
                return True
