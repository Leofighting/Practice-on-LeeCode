# -*- coding:utf-8 -*-
__author__ = "leo"

# 从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

import collections


class Solution:
    def level_order(self, root):
        if not root:
            return []
        res, queue = [], collections.deque()
        queue.append(root)

        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(tmp)
        return res
