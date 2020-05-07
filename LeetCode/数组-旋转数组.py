# -*- coding:utf-8 -*-
__author__ = "leo"


# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
# 示例 1:
# 输入: [1,2,3,4,5,6,7] 和 k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右旋转 1 步: [7,1,2,3,4,5,6]
# 向右旋转 2 步: [6,7,1,2,3,4,5]
# 向右旋转 3 步: [5,6,7,1,2,3,4]


class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k %= n
        for _ in range(k):
            nums.insert(0, nums.pop())


class Solution1:
    def rotate(self, nums, k):
        n = len(nums)
        k %= n
        nums[:] = nums[-k:] + nums[: -k]
