# -*- coding:utf-8 -*-
__author__ = "leo"


# 请完成一个函数，输入一个二叉树，该函数输出它的镜像。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mirror_tree(self, root):
        if not root:
            return
        root.left, root.right = self.mirror_tree(root.right), self.mirror_tree(root.left)
        return root


class Solution1:
    def mirror_tree(self, root):
        if not root:
            return

        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            node.left, node.right = node.right, node.left

        return root
