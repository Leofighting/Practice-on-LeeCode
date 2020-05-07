# -*- coding:utf-8 -*-
__author__ = "leo"

# 输入一个链表，按链表从尾到头的顺序返回一个ArrayList。


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    @staticmethod
    def print_list_from_tail_to_head(list_node):
        lst = []
        head = list_node
        while head:
            lst.insert(0, head.val)
            head = head.next
        return lst
