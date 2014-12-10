class Solution:
	# @return a boolean
	def isPalindrome(self, x):
		l = len(str(x))
		p = 0
		q = l - 1
		while p <= q:
			if x[p] != x[q]:
				return False
			p += 1
			q -= 1

		return True

A = Solution()
print A.isPalindrome(1221)
