# -*- coding:utf-8 -*-
__author__ = "leo"


# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
# 示例 1:
# 输入: 1->1->2
# 输出: 1->2


class Solution:
    def delete_duplicates(self, head):
        if not (head and head.next):
            return head

        i, j = head, head

        while j:
            if i.val != j.val:
                i = i.next
                i.val = j.val
            j = j.next

        i.next = None
        return head
