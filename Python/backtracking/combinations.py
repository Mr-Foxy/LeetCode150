class Solution:
	def __init__(self):
		self.res = []

	# @return a list of lists of integers
	def combine(self, n, k):
		num = range(1, n + 1)
		self.combine_AUX([], k, num, 0)
		return self.res
	
	def combine_AUX(self, cur, l, num, cur_i):
		l_a = len(num)
		if len(cur) == l:
			self.res.append(list(cur))
			return

		for i in range(cur_i, l_a):
			cur.append(num[i])
			self.combine_AUX(cur, l, num, i + 1)
			cur.pop()

A = Solution()
print A.combine(4,2)
