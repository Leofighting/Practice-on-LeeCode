给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

示例 1:

给定 nums = [3,2,2,3], val = 3,

函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。

你不需要考虑数组中超出新长度后面的元素。
示例 2:

给定 nums = [0,1,2,2,3,0,4,2], val = 2,

函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。

注意这五个元素可为任意顺序。

你不需要考虑数组中超出新长度后面的元素。



class Solution(object):
    def remove_element(self, nums, val):
        """

        :param nums: list()
        :param val: int
        :return: int
        """
        # 第一种方法
        # left = 0
        # right = len(nums) - 1
        # while left < right:
        #     if nums[left] == val and nums[right] != val:
        #         nums[left], nums[right] = nums[right], nums[left]
        #         left += 1
        #         right -= 1
        #     elif nums[right] == val:
        #         right -= 1
        #     elif nums[left] != val:
        #         left += 1
        # result = 0
        # for i in range(len(nums)):
        #     if nums[i] != val:
        #         result += 1
        #     else:
        #         return result, nums[: result]

        # 第二种方法
        while True:
            if val in nums:
                nums.remove(val)
            else:
                return len(nums), nums[: len(nums)]


test = Solution()
print(test.remove_element([1, 3, 2, 4, 2, 4, 2, 1], 2))
