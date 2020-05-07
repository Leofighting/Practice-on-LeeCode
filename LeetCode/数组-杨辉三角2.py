# -*- coding:utf-8 -*-
__author__ = "leo"


# 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。


class Solution:
    @staticmethod
    def get_row(row_index):
        r = [1]
        for i in range(1, row_index + 1):
            r.insert(0, 0)
            for j in range(i):
                r[j] = r[j] + r[j + 1]
        return r
