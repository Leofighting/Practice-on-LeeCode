实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:

输入: haystack = "hello", needle = "ll"
输出: 2
示例 2:

输入: haystack = "aaaaa", needle = "bba"
输出: -1


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 方法一：利用切片相等的原理
        # for i in range(0, (len(haystack) - len(needle) + 1)):
        #     if haystack[i: i + len(needle)] == needle:
        #         return i
        # return -1 
        # 方法二：find()函数
        return haystack.find(needle)
        
