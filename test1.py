# -*- coding:utf-8 -*-
__author__ = "leo"


class Solution:
    def find_first_index(self, nums):
        lst = []
        for num in nums:
            if num not in lst:
                lst.append(num)
            else:
                return lst.index(num)
        return None


# t = Solution()
# print(t.find_first_index([1, 2, 3, 4, 5, 6, 3]))


class Solution1:
    def is_palindrome(self, x):
        return str(x) == str(x)[::-1]

    def is_palindrome1(self, x):
        x = str(x)
        left = 0
        right = len(x) - 1
        while left <= right:
            if x[left] != x[right]:
                return False
            else:
                left += 1
                right -= 1
        return True


x = 1233456
x = str(x)
print(x[1])
