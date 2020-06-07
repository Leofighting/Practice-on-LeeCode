# -*- coding:utf-8 -*-
__author__ = "leo"


# 给定一个二叉树，检查它是否是镜像对称的。


class Solution:
    def is_symmetric(self, root):
        if not root:
            return True

        def is_same(t1, t2):
            if t1 and t2:
                return t1.val == t2.val and is_same(t1.left, t2.right) and is_same(t1.right, t2.left)
            elif not t1 and not t2:
                return True
            else:
                return False

        return is_same(root.left, root.right)
