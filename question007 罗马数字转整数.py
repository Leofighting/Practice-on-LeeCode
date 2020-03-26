罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。


class Solution:
    def romanToInt(self, s: str) -> int:
        roma_nums = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        num = 0
        for i in range(len(s)-1):
            if roma_nums[s[i]] >= roma_nums[s[i+1]]:
                num += roma_nums[s[i]]
            else:
                num -= roma_nums[s[i]]
        last_num = roma_nums[s[len(s)-1]]
        num += last_num
        return num
