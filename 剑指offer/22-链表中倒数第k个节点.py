# -*- coding:utf-8 -*-
__author__ = "leo"


# 输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。
# 例如，一个链表有6个节点，从头节点开始，它们的值依次是1、2、3、4、5、6。这个链表的倒数第3个节点是值为4的节点。


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def get_kth_form_end(self, head, k):
        former, latter = head, head

        for _ in range(k):
            if not former:
                return
            former = former.next

        while former:
            former, latter = former.next, latter.next

        return latter
