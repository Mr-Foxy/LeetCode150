class Solution:
	# @return a tuple, (index1, index2)
	def twoSum(self, num, target):
		dict_num = dict()
		
		for i in num:
			dict_num[i] = 1

		for j in range(len(num)):
			if not target - num[j] in dict_num:
				continue
			for k in range(j + 1, len(num)):
				if num[j] + num[k] == target:
					return (j + 1, k + 1)
			
A = Solution()
num = [2, 7, 11, 15]
target = 9
print A.twoSum(num, target)
