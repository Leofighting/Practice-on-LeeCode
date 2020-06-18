# -*- coding:utf-8 -*-
__author__ = "leo"


# 给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。
# 对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。
# 你可以返回任何满足上述条件的数组作为答案。


class Solution:
    def sort_arry_by_parity(self, A):
        pos = 0
        for i in range(1, len(A), 2):
            if A[i] % 2 == 0:
                while A[pos] % 2 == 0:
                    pos += 2
                A[pos], A[i] = A[i], A[pos]
                pos += 2

        return A
