给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



class Solution:
    def reverse(self, x: int) -> int:
        str_num = str(x)
        if str_num.startswith("-"):
            str_num1 = str_num[1:]
            result = int("-"+str_num1[::-1])
            if result < -2 ** 31:
                return 0
            return result
        else:
            result = int(str_num[::-1])
            if result > 2 **31 - 1:
                return 0
            return result
        

test = Solution()
result = test.reverse(-123)
print(result)


解题思路：
1 转化为字符串str()
2 利用列表的逆向输出功能list[::-1]
3 startswith()
