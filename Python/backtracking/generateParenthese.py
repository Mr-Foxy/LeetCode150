class Solution:
	def __init__(self):
		self.res = []
  # @param an integer
  # @return a list of string
	def generateParenthesis(self, n):
		l = 2 * n
		self.generateParenthesis_AUX(0, 0, [], n)
		return self.res
		
	def generateParenthesis_AUX(self, left, right, cur, n):
		if left == n and right == n:
			self.res.append(''.join(cur))
			return
		
		if left + 1 <= n:
			cur.append("(")
			self.generateParenthesis_AUX(left + 1, right, cur, n)
			cur.pop()
		
		if right < left:
			cur.append(")")
			self.generateParenthesis_AUX(left, right + 1, cur, n)
			cur.pop()

A = Solution()
print A.generateParenthesis(3)

