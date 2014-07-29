class Solution:
    # @return an integer
    def numDistinct(self, S, T):
			len_S = len(S)
			len_T = len(T)
			if len_S < len_T:
				return 0
			path = [[0 for i in range(len_S + 1)] for j in range(len_T + 1)]
			for i in range(len_S + 1):
				path[0][i] = 1
			
			for j in range(1, len_S + 1):
				for i in range(1, len_T + 1):
					path[i][j] = path[i][j-1] + (path[i-1][j-1] if T[i-1] == S[j-1] else 0)

			print path
			return path[i][j]

#a = Solution()
#print a.numDistinct("rabbbit", "rabbit") 

