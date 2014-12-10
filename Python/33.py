class Solution:
	# @return a list of integers
	def getRow(self, rowIndex):
		if rowIndex == 0:
			return []
		tmp = [1]
		for i in range(1,rowIndex + 1):
			tmp = [0] + tmp + [0]
			new = []
			for j in range(len(tmp) - 1):
				new.append(tmp[j] + tmp[j + 1])
			tmp = new

		return tmp

a = Solution()
print a.getRow(3)

