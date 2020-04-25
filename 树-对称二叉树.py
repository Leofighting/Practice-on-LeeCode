# -*- coding:utf-8 -*-
__author__ = "leo"

# 给定一个二叉树，检查它是否是镜像对称的。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def is_symmetric(self, root):
        if not root:
            return True

        def dfs(left, right):
            if not (left or right):
                return True
            if not (left and right):
                return False
            if left.val != right.val:
                return False

            return dfs(left.left, right.right) and dfs(left.right, right.left)

        return dfs(root.left, root.right)
