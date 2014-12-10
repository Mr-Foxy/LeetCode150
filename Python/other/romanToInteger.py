import pdb
class Solution:
  # @return an integer
  def romanToInt(self, s):
		res = 0
		l = len(s)
		for i in range(l):
			#pdb.set_trace()
			if s[i] == 'I':
				res += 1

			if s[i] == 'V':
				if i > 0 and s[i-1] == 'I':
					res += 3
				else:
					res += 5

			if s[i] == 'X':
				if i > 0 and s[i-1] == 'I':
					res += 8
				else:
					res += 10

			if s[i] == 'L':
				if i > 0 and s[i-1] == 'X':
					res += 30
				else:
					res += 50

			if s[i] == 'C':
				if i > 0 and s[i-1] == 'X':
					res += 80
				else:
					res += 100

			if s[i] == 'D':
				if i > 0 and s[i-1] == 'C':
					res += 300
				else:
					res += 500

			if s[i] == 'M':
				if i > 0 and s[i-1] == 'C':
					res += 800
				else:
					res += 1000

		return res

a = Solution()
print a.romanToInt("XXXIV")
