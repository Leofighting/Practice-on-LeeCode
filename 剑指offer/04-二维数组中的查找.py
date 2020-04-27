# -*- coding:utf-8 -*-
__author__ = "leo"

# 在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。


class Solution:
    def findNumberIn2DArray(self, matrix, target):
        rows = len(matrix)
        if rows == 0:
            return False

        cols = len(matrix[0])

        if cols == 0:
            return False

        x, y = 0, cols - 1

        while x < rows and y >= 0:
            if target == matrix[x][y]:
                return True
            elif target < matrix[x][y]:
                y -= 1
            else:
                x += 1

        return False


