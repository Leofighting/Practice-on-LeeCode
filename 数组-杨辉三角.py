# -*- coding:utf-8 -*-
__author__ = "leo"


# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
# 在杨辉三角中，每个数是它左上方和右上方的数的和。

class Solution:
    @staticmethod
    def generate(num_rows):
        if num_rows == 0:
            return []
        res = [[1]]
        while len(res) < num_rows:
            new_row = [a + b for a, b in zip(res[-1] + [0], [0] + res[-1])]
            res.append(new_row)
        return res
