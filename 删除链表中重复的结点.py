# -*- coding:utf-8 -*-
__author__ = "leo"

# 在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
# 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def delete_duplication(self, p_head):
        if p_head is None or p_head.next is None:
            return p_head
        head = p_head.next

        if head.val != p_head.val:
            p_head.next = self.delete_duplication(p_head.next)
        else:
            while p_head.val == head.val and head.next is not None:
                head = head.next
            if head.val != p_head.val:
                p_head = self.delete_duplication(head)
            else:
                return None
        return p_head
