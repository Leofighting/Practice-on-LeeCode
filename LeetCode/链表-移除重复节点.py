# -*- coding:utf-8 -*-
__author__ = "leo"


# 编写代码，移除未排序链表中的重复节点。保留最开始出现的节点。
# 示例1:
#  输入：[1, 2, 3, 3, 2, 1]
#  输出：[1, 2, 3]


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def remove_duplicate_nodes(self, head):
        if not head:
            return head

        node_set = {head.val}
        prev, cur = head, head.next

        while cur:
            if cur.val in node_set:
                prev.next = cur.next
                del cur
                cur = prev.next
            else:
                node_set.add(cur.val)
                prev, cur = cur, cur.next

        return head
