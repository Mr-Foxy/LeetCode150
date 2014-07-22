# Palindrome Partitioning II
import pdb
class Solution:
	# @param s, a string
	# @return a list of lists of string
	def minCut(self, s):
		l = len(s)
		A = [None] * l 
		p_table = []
		for i in range(l):
			new = []
			for j in range(l):
				new.append(-1)
			p_table.append(new)
		

		for i in range(l):
			p_table[i][i] = 1

		i = l - 1
		while i >=  0:
			if self.palindrome_dp(s, p_table, i, l-1):
				A[i] = [l]
			else:
				A[i] = []


			for j in range(i+1, l):
				if A[j] and self.palindrome_dp(s, p_table, i, j-1):
					A[i].append(j)

			for k in p_table:
				print k
		
			i -= 1

		print A
		res = []
		path_list = [[0]]
		while path_list:
			new_list = []
			for path in path_list:
				if path[-1] == l:
					res.append(len(path))
				else:
					for i in A[path[-1]]:
						new_list.append(path + [i])
			path_list = new_list

		return min(res) - 2

	def palindrome_dp(self, s, table, i, j):
		if i > j:
			return True
		if table[i][j] == -1:
			#pdb.set_trace()
			if self.palindrome_dp(s, table, i+1, j-1) and s[i] == s[j]:
				table[i][j] = 1
				return True
			else:
				table[i][j] = 0
				return False
		elif table[i][j] == 1:
			return True
		else:
			return False

# no Use now
'''
	def palindrome(self, s):
		length = len(s)
		mid = length / 2
		result = True
		for f in range(0, mid):
			b = -f - 1
			if s[f] != s[b]:
				return False
		return True
'''

a = Solution()
print a.minCut("abacc")
