# -*- coding:utf-8 -*-
__author__ = "leo"


# 我们正在玩一个猜数字游戏。 游戏规则如下：
# 我从 1 到 n 选择一个数字。 你需要猜我选择了哪个数字。
# 每次你猜错了，我会告诉你这个数字是大了还是小了。
# 你调用一个预先定义好的接口 guess(int num)，它会返回 3 个可能的结果（-1，1 或 0）：
#
# -1 : 我的数字比较小
#  1 : 我的数字比较大
#  0 : 恭喜！你猜对了！


def guess(num: int) -> int:
    pass


class Solution:
    def guess_number(self, n):
        i = 1
        j = n
        while i <= j:
            mid = (i + j) // 2
            res = guess(mid)
            if res == 0:
                return mid
            elif res == -1:
                j = mid - 1
            else:
                i = mid + 1

        return -1
