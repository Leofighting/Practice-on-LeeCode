# -*- coding:utf-8 -*-
__author__ = "leo"

# 请实现一个函数，用来判断一颗二叉树是不是对称的。
# 注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def is_symmetrical(self, p_root):
        if not p_root:
            return True
        return self.is_same(p_root.left, p_root.right)

    def is_same(self, p1, p2):
        if not p1 and not p2:
            return True
        if not p1 and p2:
            return False
        if p1 and not p2:
            return False
        return self.is_same(p1.legt, p2.right) and self.is_same(p1.right, p2.left) and p1.val == p2.val
