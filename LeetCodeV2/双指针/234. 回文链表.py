# -*- coding:utf-8 -*-
__author__ = "leo"


# 请判断一个链表是否为回文链表。


class Solution:
    def is_palindrome(self, head):
        lst = []
        while head is not None:
            lst.append(head.val)
            head = head.next
        return lst == lst[::-1]
