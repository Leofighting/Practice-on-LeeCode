# -*- coding:utf-8 -*-
__author__ = "leo"

# 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。
# 示例 1:
# 输入: "hello"
# 输出: "holle"


class Solution:
    def reverse_vowels(self, s):
        arr = list(s)
        vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        p1, p2 = 0, len(arr) - 1

        while p1 < p2:
            while arr[p1] not in vowel and p1 < p2:
                p1 += 1
            while arr[p2] not in vowel and p1 < p2:
                p2 -= 1

            if p1 < p2:
                arr[p1], arr[p2] = arr[p2], arr[p1]
                p1 += 1
                p2 -= 1

        return "".join(arr)
