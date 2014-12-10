class Solution:
  # @param s, a string
  # @return an integer
	def lengthOfLastWord(self, s):
		l_split = s.split()
		if not l_split:
			return 0
		else:
			return len(l_split[-1])

A = Solution()
print A.lengthOfLastWord(" ")
        
