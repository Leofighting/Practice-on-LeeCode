# -*- coding:utf-8 -*-
__author__ = "leo"


# 请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。


class Solution:
    def is_symmetric(self, root):
        if not root:
            return True

        def is_mirror(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val == q.val:
                return is_mirror(p.left, q.right) and is_mirror(p.right, q.left)
            else:
                return False

        return is_mirror(root, root)