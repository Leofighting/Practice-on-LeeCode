给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true


class Solution:
    def isValid(self, s: str) -> bool:
        left = ['(', '[', '{']
        right = [')', ']', '}']
        mapping = dict(zip(left, right))
        stack = []
        for i in s:
            if len(stack) == 0 or i in left:   # 栈为空或字符为左括号则进栈
                stack.append(i)
            elif (stack[-1] in left) and (mapping[stack[-1]] == i):
                # 若栈中最后一个字符为左括号并且i为与之对应的右括号
                stack.pop()     # 将栈中上面的元素出栈
            else:
                return False
        if len(stack) == 0:     # 若遍历结束后栈为空说明全部匹配成功
            return True
        else:
            return False        # 否则有未匹配的括号，返回False


test = Solution()
result = test.isValid("({)}")
print(result)
