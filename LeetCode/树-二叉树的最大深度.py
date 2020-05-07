# -*- coding:utf-8 -*-
__author__ = "leo"


# 给定一个二叉树，找出其最大深度。
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
# 说明: 叶子节点是指没有子节点的节点。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def max_depth(self, root):
        if root is None:
            return 0
        else:
            left_height = self.max_depth(root.left)
            right_height = self.max_depth(root.right)
            return max(left_height, right_height) + 1


class Solution1:
    def max_depth(self, root):
        stack = []
        if root is not None:
            stack.append((1, root))

        depth = 0

        while stack:
            current_depth, root = stack.pop()
            if root is not None:
                depth = max(depth, current_depth)
                stack.append((current_depth + 1, root.left))
                stack.append((current_depth + 1, root.right))

        return depth
