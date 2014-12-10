class Solution:
	# @return a string
	def longestCommonPrefix(self, strs):
		prefix = []
		
		if len(strs) == 0:
			return ""
		if len(strs) == 1:
			return strs[0]
		j = 0
		while True:
			if len(strs[0]) - 1 >= j:
				prefix.append(strs[0][j])
			else:
				return ''.join(prefix)
			for i in range(1, len(strs)):
				strLen = len(strs[i])
				if strLen - 1 < j:
					prefix.pop()
					return ''.join(prefix)

				if strs[i][j] != prefix[j]:
					prefix.pop()
					return ''.join(prefix)
			j += 1

		return ""
	
A = Solution()
test = ["abc", "abcde"]
print A.longestCommonPrefix(test)
