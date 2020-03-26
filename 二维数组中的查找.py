# 在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
# 请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

class Solution:
	def Find(self, target, array):
		n = len(array)
		flag = False

		for i in range(n):
			if target in array[i]:
				flag = True
				break
		return flag


while True:
	try:
		s = Solution()
		lst = list(eval(input()))
		target = lst[0]
		array = lst[1]
		print(s.Find(target, array))
	except:
		break