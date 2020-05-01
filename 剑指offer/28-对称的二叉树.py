# -*- coding:utf-8 -*-
__author__ = "leo"


# 请实现一个函数，用来判断一棵二叉树是不是对称的。
# 如果一棵二叉树和它的镜像一样，那么它是对称的。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def is_symmetric(self, root):
        def recur(L, R):
            if not L and not R:
                return True
            if not L or not R or L.val != R.val:
                return False
            return recur(L.left, R.right) and recur(L.right, R.left)

        return recur(root.left, root.right) if root else True
