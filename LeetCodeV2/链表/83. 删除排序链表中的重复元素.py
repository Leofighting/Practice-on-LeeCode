# -*- coding:utf-8 -*-
__author__ = "leo"


# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。


class Solution:
    def delete_duplicates(self, head):
        dicts = {}
        p = head
        last = None
        while p is not None:
            if p.val in dicts:
                if last is None:
                    head = p.next
                else:
                    last.next = p.next
                    p = last.next
            else:
                dicts[p.val] = 1
                last = p
                p = p.next

        return head


class Solution1:
    def delete_duplicates(self, head):
        cur = head
        nums = set()
        pre = None

        while cur:
            if cur.val in nums:
                pre.next = cur.next
            else:
                nums.add(cur.val)
                pre = cur
            cur = cur.next

        return head
