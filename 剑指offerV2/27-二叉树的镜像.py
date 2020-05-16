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
        if root:
            root.left, root.right = self.mirror_tree(root.right), self.mirror_tree(root.left)
        return root
