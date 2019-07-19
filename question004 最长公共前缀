编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 “”。

示例 1:

输入: [“flower”,“flow”,“flight”]
输出: “fl”
示例 2:

输入: [“dog”,“racecar”,“car”]
输出: “”
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-common-prefix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
--------------------- 
作者：xiJao文 
来源：CSDN 
原文：https://blog.csdn.net/fenqi1989/article/details/96486932 
版权声明：本文为博主原创文章，转载请附上博文链接！


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        elif len(strs) == 1:
            return strs[0]
        else:
            minlen = len(min(strs, key=len))
            s = ""
            for i in range(1, minlen+1):
                if len({s[:i] for s in strs}) == 1:
                    s = max(s, strs[0][:i])
            return s
        
        
解题思路：
1 集合的特性
