class Solution:
	# @param obstacleGrid, a list of lists of integers
	# @return an integer
	def uniquePathsWithObstacles(self, obstacleGrid):
		m = len(obstacleGrid)
		n = len(obstacleGrid[0])

		dp = [[0 for j in range(n)] for i in range(m)]
		dp[0][0] = 1
		
		for i in range(m):
			for j in range(n):
				if obstacleGrid[i][j] == 1:
					dp[i][j] = 0
					continue
				if i - 1 >= 0:
					dp[i][j] += dp[i-1][j]
				if j - 1 >= 0:
					dp[i][j] += dp[i][j-1]

		return dp[m-1][n-1]
