class Solution:
  # @return an integer
  def numTrees(self, n):
		if n == 0:
			return 0
		l = [0 for i in range(n + 1)]
		l[0] = 1
		l[1] = 1
		for i in range(2, n+1):
			cur = i - 1
			for j in range(i):
				l[i] += l[j] * l[cur - j]
		return l[n]

a = Solution()
print a.numTrees(3)
