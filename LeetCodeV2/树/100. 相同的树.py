# -*- coding:utf-8 -*-
__author__ = "leo"


# 给定两个二叉树，编写一个函数来检验它们是否相同。
#
# 如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

class Solution:
    def is_same_tree(self, p, q):
        if p is None and q is None:
            return True
        if p is not None and q is not None:
            return p.val == q.val and self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right)
        else:
            return False

