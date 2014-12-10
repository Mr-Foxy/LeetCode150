class Solution:
	# @param A, a list of integers
	# @return an integer
	def firstMissingPositive(self, A):
		min_positive = float('inf')
		num = dict()
		for i in A:
			num[i] = 1
			if i > 0 and i < min_positive:
				min_positive = i

		if min_positive != 1:
			return 1

		i = min_positive
		while True:
			if num.get(i, 0) == 0:
				return i
			i += 1

A = Solution()
print A.firstMissingPositive([])
