class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
		if numRows == 0:
			return []
		res = [[1]]
		for i in range(1,numRows):
			tmp = res[i-1]
			tmp = [0] + tmp + [0]
			new = []
			for j in range(len(tmp) - 1):
				new.append(tmp[j] + tmp[j + 1])
			res.append(new)

		return res

a = Solution()
print a.generate(5)
				
				
