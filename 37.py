class Solution:
    # @return an integer
    def numDistinct(self, S, T):
		diff = []
		j = 0 
		for i in range(len(T)):
			if T[i] != S[j]:
				start = j
				while T[i] != S[j]:
					j += 1
				end = j
				diff.append([start, end])
			j += 1

		res = 1
		for word_range in diff:
			key = S[word_range[0]:word_range[1]]
			key_len = len(key)
			repeat_range = word_range
			count = 1
			while repeat_range[0] >= 0:
				repeat_range[0] -= key_len
				repeat_range[1] -= key_len
				if S[repeat_range[0]:repeat_range[1]] != key:
					res *= pow(2, count)
					break
				count += 1
			return res
				
a = Solution()
print a.numDistinct("rabbbit", "rabbit") 

