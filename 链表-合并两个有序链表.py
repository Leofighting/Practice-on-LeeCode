# -*- coding:utf-8 -*-
__author__ = "leo"

# 将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
# 示例：
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def merge_two_lists(self, l1, l2):
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
                l1.next = self.merge_two_lists(l1.next, l2)
        return l1 or l2


class Solution1:
    def merge_two_lists(self, l1, l2):
        prehead = ListNode(-1)
        prev = prehead

        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        return prehead.next
    