class Solution:
	# @param num, a list of integer
	# @return a list of integer
	def nextPermutation(self, num):
		l = len(num)
		if l <= 1:
			return num

		j = l - 2
		while j >= 0:
			if num[j] < num[j+1]:
				break
			j -= 1

		i = l - 1
		if j >= 0:
			while num[i] <= num[j]:
				i -= 1
			num[i], num[j] = num[j], num[i]
		num[j+1:] = num[j+1:][::-1]
		
		return num

A = Solution()
print A.nextPermutation([1,5,1])

