class Solution:
	# @return an integer
	def uniquePaths(self, m, n):
		dp = [[0 for j in range(n)]for i in range(m)]
		dp[0][0] = 1
		
		for i in range(m):
			for j in range(n):
				if i - 1 >= 0:
					dp[i][j] += dp[i-1][j]
				if j - 1 >= 0:
					dp[i][j] += dp[i][j-1]

		return dp[m-1][n-1]

A = Solution()
print A.uniquePaths(2,3)
        
