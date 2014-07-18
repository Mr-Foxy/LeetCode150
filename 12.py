import pdb
class Solution:
	# @param s, a string
	# @param dict, a set of string
	# @return a boolean
	def wordBreak(self, s, dict):
		n = len(s) 
		table = [None] * n
		i = n - 1
		while i >= 0:
			#if i == 1:
			#	pdb.set_trace()
			if s[i:n] in dict:
				table[i] = [n]
			else:
				table[i] = []
			for j in xrange(i+1,n):
				if s[i:j] in dict and table[j]:
					table[i].append(j)
			i -= 1

		print table

		res = []
		path_list = [[0]]

		while path_list:
			new_list = []

			for path in path_list:
				if path[-1] == n:
					tmp = [s[path[i]:path[i+1]] for i in range(0, len(path) - 1)]
					res.append(" ".join(tmp))
				else:
					for i in table[path[-1]]:
						new_list.append(path + [i])

			path_list = new_list
			print path_list

		return res
		
		# My Creepy Solution
		'''
		#pdb.set_trace()
		for l in range(1, n + 1):
			for i in range(0, n - l + 1):
				j = i + l - 1
				q = False
				for k in range(i, j - 1 + 1):
					q = q or ( table[i][k] and table[k+1][j] )
					if table[i][k] and table[k+1][j] == True:
						result_table[i][j].append( str(i) + str(k) + str(k+1) + str(j) )
						
				if q == False:
					tmp = s[i : j+1]
					for words in dict:
						if words == tmp:
							q = True
							result_table[i][j].append("*")

				table[i][j] = q

		for x in table:
			print x
		print "result table is"
		for x in result_table:
			print x

		return table[0][len(s) - 1]
		'''

def main():
	dict = []
	str = "a"
	a = Solution()
	print a.wordBreak(str,dict)
if __name__ == '__main__':
	main()
