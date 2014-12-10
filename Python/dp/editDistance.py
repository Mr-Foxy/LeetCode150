class Solution:
  # @return an integer
  def minDistance(self, word1, word2):
		len1 = len(word1)
		len2 = len(word2)
		if len1 == 0:
			return len2
		if len2 == 0:
			return len1

		dp = [[0 for i in range(len2 + 1)] for i in range(len1 + 1)]
		
		for i in range(len1 + 1):
			dp[i][0] = i
		for i in range(len2 + 1):
			dp[0][i] = i
		
		for i in range(1, len1 + 1):
			for j in range(1, len2 + 1):
				sub = dp[i - 1][j - 1]
				if word1[i-1] != word2[j-1]:
					sub += 1
				dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, sub)

		return dp[len1][len2]



a = Solution()
print a.minDistance("ab", "a")
