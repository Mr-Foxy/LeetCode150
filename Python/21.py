class Solution:
	# @param s, a string
	# @return a list of lists of string
	def partition(self, s):
		l = len(s)
		A = [None] * l 
		i = l - 1
		while i >=  0:
			if self.palindrome(s[i:l]):
				A[i] = [l]
			else:
				A[i] = []

			for j in range(i+1,l):
				if A[j] and self.palindrome(s[i:j]):
					A[i].append(j)

			i -= 1

		print A
		
		res = []
		path_list = [[0]]
		while path_list:
			new_list = []
			for path in path_list:
				if path[-1] == l:
					tmp = [s[path[i]:path[i+1]] for i in range(0, len(path) - 1)]
					res.append(tmp)
				else:
					for i in A[path[-1]]:
						new_list.append(path + [i])
			path_list = new_list

		return res

	def palindrome(self, s):
		length = len(s)
		mid = length / 2
		result = True
		for f in range(0, mid):
			b = -f - 1
			if s[f] != s[b]:
				return False
		return True

a = Solution()
print a.partition("aab")
