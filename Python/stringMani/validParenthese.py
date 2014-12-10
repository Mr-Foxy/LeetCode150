class Solution:
	# @return a boolean
	def isValid(self, s):
		stack = []
		for i in range(len(s)):
			if s[i] == '(' or s[i] == '[' or s[i] == '{':
				stack.append(s[i])
			else:
				if not stack:
					return False
				else:
					cur = stack[-1]
					if (cur == '(' and s[i] == ')') or (cur == '[' and s[i] == ']') or (cur == '{' and s[i] == '}'):
						stack.pop()
						continue
					else:
						return False
		if stack:
			return False
		return True


A = Solution()
print A.isValid("[")
