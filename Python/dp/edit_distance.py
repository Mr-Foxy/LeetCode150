class Solution:
  # @return an integer
  def minDistance(self, word1, word2):
		if not word1 and not word2:
			return 0

		len1 = len(word1)
		len2 = len(word2)

		if not word1 or not word2:
			return abs(len1 - len2)

		table = []
		cur = []
		for i in range(len1 + 1):
			for j in range(len2 + 1):
				cur.append(0)
			table.append(cur)
			cur = []
		
		for i in range(1, len1 + 1):
			for j in range(1, len2 + 1):
				if word1[i - 1] == word2[j - 1]:
					table[i][j] = table[i-1][j-1] + 1
				else:
					table[i][j] = max(table[i-1][j], table[i][j-1])

		print table
		str = table[len1][len2]
		return max(len1, len2) - str 

a = Solution()
print a.minDistance("ab", "bc")

			
        
