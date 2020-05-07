# -*- coding:utf-8 -*-
__author__ = "leo"


# 删除链表中等于给定值 val 的所有节点。
# 示例:
# 输入: 1->2->6->3->4->5->6, val = 6
# 输出: 1->2->3->4->5


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def remove_elements(self, head, val):
        sentinel = ListNode(0)
        sentinel.next = head
        prev, curr = sentinel, head

        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return sentinel.next