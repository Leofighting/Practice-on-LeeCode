# -*- coding:utf-8 -*-
__author__ = "leo"


# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
# 说明：本题中，我们将空字符串定义为有效的回文串。


class Solution:
    def is_palindrome(self, s):
        alpha_filter = filter(str.isalnum, s)
        ste = "".join(alpha_filter)
        ste1 = ste[::-1]
        if ste.upper() == ste1.upper():
            return True
        return False


class Solution1:
    def is_palindrome(self, s):
        import re
        s1 = re.sub(r"[^A-Za-z0-9]", "", s).lower()
        p1 = 0
        p2 = len(s1) - 1
        while p1 <= p2:
            if s1[p1] == s1[p2]:
                p1 += 1
                p2 -= 1
            else:
                return False
        return True
