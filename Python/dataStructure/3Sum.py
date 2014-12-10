class Solution:
	# @return a list of lists of length 3, [[val1,val2,val3]]
	def threeSum(self, num):
		num.sort()
		res = []
		cur = []
		l = len(num)
		i = 0
		while i < l - 2:
			if i > 0 and num[i] == num[i-1]:
				i += 1
				continue

			j = i + 1
			k = l - 1
			while j < k:
				temp = num[i] + num[j] + num[k]
				if temp == 0:
					cur = [num[i], num[j], num[k]]
					res.append(cur)
					j += 1
					k -= 1

					while j < k and num[j] == num[j-1]:
						j += 1
					while j < k and num[k] == num[k+1]:
						k -= 1

				elif temp < 0:
					j += 1
				else:
					k -= 1 

			
			i += 1
		return res

A= Solution()
print A.threeSum([-1,0,1,2,-1,-4])

