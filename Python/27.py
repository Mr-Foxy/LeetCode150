import pdb
class Solution:
	# @param s, a string
	# @return a boolean
	def isPalindrome(self, s):
		i = 0
		j = len(s) - 1
		res = True
		pdb.set_trace()

		while i < j:
			while (not str.isalpha(s[i]) and not str.isdigit(s[i])) and i < j:
				i += 1

			front = s[i].lower()

			if i >= j:
				return True

			while (not str.isalpha(s[j]) and not str.isdigit(s[j])) and i < j:
				j -= 1

			if i >= j:
				return True

			rear = s[j].lower()
			
			if front != rear:
				return False

			i += 1
			j -= 1

		return True

a = Solution()
print a.isPalindrome("ab")
