# -*- coding:utf-8 -*-
__author__ = "leo"


# 输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。例如，一个链表有6个节点，从头节点开始，它们的值依次是1、2、3、4、5、6。这个链表的倒数第3个节点是值为4的节点。


class Solution:
    def get_kth_from_end(self, head, k):
        pre = None
        cur = head
        while cur is not None:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp

        cur = pre
        pre = None

        while k > 0:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
            k -= 1

        return pre


class Solution1:
    def get_kth_from_end(self, head, k):
        i, j = head, head
        while k - 1:
            j = j.next
            k -= 1

        while j.next:
            i = i.next
            j = j.next

        return i
