# -*- coding:utf-8 -*-
__author__ = "leo"

# 请实现一个函数按照之字形打印二叉树
# 即第一行按照从左到右的顺序打印
# 第二层按照从右至左的顺序打印
# 第三行按照从左到右的顺序打印
# 其他行以此类推。

from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    @staticmethod
    def print_val(p_root):
        if not p_root:
            return []
        res, tmp = [], []
        last = p_root
        q = deque([p_root])
        left_to_right = True

        while q:
            t = q.popleft()
            tmp.append(t.val)
            if t.left:
                q.append(t.left)
            if t.right:
                q.append(t.right)
            if t == last:
                res.append(tmp if left_to_right else tmp[::-1])
                left_to_right = not left_to_right
                tmp = []
                if q:
                    last = q[-1]
        return res
