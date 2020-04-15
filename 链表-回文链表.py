# -*- coding:utf-8 -*-
__author__ = "leo"


# 请判断一个链表是否为回文链表。
# 示例 1:
# 输入: 1->2
# 输出: false
# 示例 2:
# 输入: 1->2->2->1
# 输出: true


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def is_palindrome(self, head):
        vals = []
        current_node = head

        while current_node is not None:
            vals.append(current_node.val)
            current_node = current_node.next

        return vals == vals[::-1]
