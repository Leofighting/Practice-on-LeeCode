给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。


# class Solution(object):
#     def max_sub_array(self, nums):
#         # 第一种方法
#         tmp = nums[0]
#         max1 = tmp
#         n = len(nums)
#         for i in range(1, n):
#             # 如果当前序列加上此时的元素的值大于tmp的值
#             # 说明最大序列和可能出现在后续序列中，记录此时的最大值
#             if tmp + nums[i] > nums[i]:
#                 max1 = max(max1, tmp + nums[i])
#                 tmp = tmp + nums[i]
#             else:
#                 # 当tmp（当前和）小于下一个元素时，当前最长序列到此为止。
#                 # 以该元素的起点继续找最大子序列，并记录此时的最大值
#                 max1 = max(max1, tmp, tmp+nums[i], nums[i])
#                 tmp = nums[i]
#         return max1


# 第二种方法
class Solution(object):
    def max_sub_array(self, nums):
        n = len(nums)
        # 递归终止条件
        if n == 1:
            return nums[0]
        else:
            # 递归计算左半边最大子序和
            max_left = self.max_sub_array(nums[0: len(nums)//2])
            # 递归计算右半边最大子序和
            max_right = self.max_sub_array(nums[len(nums)//2: len(nums)])
        # 计算中间的最大子序和，从右到左计算左边的最大子序和，从左到右计算右边的最大子序和，再相加
        max_l = nums[len(nums)//2-1]
        tmp = 0
        for i in range(len(nums)//2-1, -1, -1):
            tmp += nums[i]
            max_l = max(tmp, max_l)
        max_r = nums[len(nums)//2]
        tmp = 0
        for i in range(len(nums)//2, len(nums)):
            tmp += nums[i]
            max_r = max(tmp, max_r)
        # 返回三个中的最大值
        return max(max_right, max_left, max_l+max_r)


test = Solution()
result = test.max_sub_array([1, -3, 4, 2, 4, -3, -1, -2, 5])
print(result)
