# -*- coding:utf-8 -*-
__author__ = "leo"


# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
# 有效字符串需满足：
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。


class Solution:
    def is_valid(self, s):
        match_dict = {"(": ")", "{": "}", "[": "]", "?": "?"}
        stack = ["?"]
        for i in s:
            if i in match_dict:
                stack.append(i)
            elif match_dict[stack.pop()] != i:
                return False

        return len(stack) == 1


class Solution1:
    def is_valid(self, s):
        left = set(["(", "[", "{"])
        right = {")": "(", "}": "{", "]": "["}
        tmp = []

        for i in s:
            if i in left:
                tmp.append(i)
            elif tmp and tmp[-1] == right[i]:
                tmp.pop()
            else:
                return False

        return True if not tmp else False
