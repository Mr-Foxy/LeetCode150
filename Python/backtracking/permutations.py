import pdb
class Solution:
  # @param num, a list of integer
  # @return a list of lists of integers
	def __init__(self):
		self.isUsed = None
		self.res = []
		self.l = 0;

	def permute(self, num):
		if not num:
			return

		self.l = len(num)
		self.isUsed = [False for i in range(self.l)]

		self.permute_AUX(0, [], num)

		return self.res

	def permute_AUX(self, index, cur, num):
		if index == self.l:
			self.res.append(list(cur))

		for i in range(len(num)):
			if not self.isUsed[i]:
				cur.append(num[i])
				self.isUsed[i] = True
				self.permute_AUX(index + 1, cur, num)
				self.isUsed[i] = False
				cur.pop()

A = Solution()
print A.permute([1,2,3])
