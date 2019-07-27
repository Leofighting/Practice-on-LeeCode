实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:

输入: 4
输出: 2
示例 2:

输入: 8
输出: 2
说明: 8 的平方根是 2.82842..., 
     由于返回类型是整数，小数部分将被舍去。



class Solution(object):
    def my_sqrt(self, x):
        # # 第一种解法，二分查找法
        # # 为了照顾到0，把左边界设置为0
        # left = 0
        # # 为了照顾到1，把左边界设置为x//2+1
        # right = x // 2 + 1
        # while left < right:
        #     # 注意：这里一定去右中位数，如果取左中位数，代码可能会进入死循环
        #     # mid = left + (right - left + 1) // 2
        #     mid = (left + right + 1) >> 1
        #     square = mid * mid
        #
        #     if square > x:
        #         right = mid - 1
        #     else:
        #         left = mid
        # # 因为一定存在，因此无需后处理
        # return left


        # 第二种解法，牛顿法
        if x < 0:
            raise Exception("不能输入负数")
        if x == 0:
            return 0
        # 起始的时候在 1 ， 这可以比较随意设置
        cur = 1
        while True:
            pre = cur
            cur = (cur + x / cur) / 2
            if abs(cur - pre) < 1e-6:
                return int(cur)


test = Solution()
result = test.my_sqrt(9)
print(result)

