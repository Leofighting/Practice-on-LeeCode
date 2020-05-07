# -*- coding:utf-8 -*-
__author__ = "leo"

# 给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
# 注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    @staticmethod
    def get_next(p_node):
        if not p_node:
            return None

        if p_node.right:
            res = p_node.right
            while res.left:
                res = res.left
            return res
        while p_node.next:
            tmp = p_node.next
            if tmp.left == p_node:
                return tmp
            p_node = tmp
        return None
