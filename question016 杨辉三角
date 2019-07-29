给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。



在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]



class Solution(object):
    def generate(self, num_rows):
        if num_rows == 0:
            return []
        elif num_rows == 1:
            return [[1]]
        elif num_rows == 2:
            return [[1], [1, 1]]
        else:
            result = self.generate(num_rows - 1)
            tmp = [1]
            length = len(result[-1])
            for i in range(length - 1):
                tmp.append(result[-1][i] + result[-1][i+1])
            tmp.append(1)
            result.append(tmp)
            return result


test = Solution()
result = test.generate(5)
print(result)
