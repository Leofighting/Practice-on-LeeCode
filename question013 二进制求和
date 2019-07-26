给定两个二进制字符串，返回他们的和（用二进制表示）。

输入为非空字符串且只包含数字 1 和 0。

示例 1:

输入: a = "11", b = "1"
输出: "100"
示例 2:

输入: a = "1010", b = "1011"
输出: "10101"


class Solution(object):
    def add_binary(self, a, b):
        # # 第一种解法
        # return bin(int(a, 2) + int(b, 2))[2:]


        # 第二种解法
        r, p = "", 0
        d = len(b) - len(a)
        a = "0" * d + a
        b = "0" * -d + b
        for i, j in zip(a[::-1], b[::-1]):
            s = int(i) + int(j) + p
            r = str(s % 2) + r
            p = s // 2
        return "1" + r if p else r


test = Solution()
result = test.add_binary("10", "11")
print(result)
