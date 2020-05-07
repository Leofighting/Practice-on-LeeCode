给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

示例 1:

输入: [1,3,5,6], 5
输出: 2
示例 2:

输入: [1,3,5,6], 2
输出: 1
示例 3:

输入: [1,3,5,6], 7
输出: 4
示例 4:

输入: [1,3,5,6], 0
输出: 0



from typing import List
class Solution(object):
    def search_insert(self, nums, target):
        # 返回大于等于target的索引，有可能是最后一个
        size = len(nums)
        if size == 0:
            return 0

        left = 0
        # 如果target 比 nums 里所有的数都打，则最有一个数的索引 + 1 就是候选值
        # 因此，诱变剂应该是数组的长度
        right = size
        # 二分法的逻辑一定要写对，否则会出现死循环或者数组下标越界
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                assert nums[mid] >= target
                right = mid
        # 调试语句
        # print("left = {}, right = {}, mid = {}".format(left, right, mid))
        return left


test = Solution()
result = test.search_insert([1, 3, 4, 5, 7], 2)
print(result)
