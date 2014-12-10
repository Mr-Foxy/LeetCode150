class Solution:
    # @return an integer
    def reverse(self, x):
			s = str(x)
			neg = False
			if s[0] == '-':
				s = s.replace("-", "")
				neg = True
			return int(("-" if neg else "") + s[::-1])

a = Solution()
print a.reverse(-321)
