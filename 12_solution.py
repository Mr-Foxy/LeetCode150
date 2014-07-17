class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
	def wordBreak(self, s, dict):
        # Step 1: similar to word break I,
        # but A[i] is a list instead of a boolean value
		n = len(s)
		A = [None] * n
		i = n-1
		while i >= 0:
			if s[i:n] in dict:
				A[i] = [n]  # A[i] contains "n" means s[i..n-1] is a word
			else:
				A[i] = []
			#if i == 3:
				#print A
			# Check al possible j break
			for j in xrange(i+1, n):
				if A[j] and s[i:j] in dict:
					#print "A[j] is "
					#print A[j]
					A[i].append(j)
			i -= 1
		print A

		# Step 2: find all possible sequences of breaks,
		# which equals to find all paths from A[0] and stop when the break is "n".
		# So it converts to BFS on a graph, with at most n steps.
		res = []  # possible sentences with break
		path_list = [[0]]  # initially, there is only one path containing the source node
		while path_list:
			new_list = []
			# For each path,
			# 1) If the path ends with break "n", then segment the string with breaks of the path
			# 2) otherwise, expand it with all possible breaks
			for path in path_list:
				if path[-1] == n:  # segment!
					# Get words according to the breaks
					temp = [ s[path[i]:path[i+1]] for i in xrange(len(path)-1) ]
					# join words together
					res.append(" ".join(temp))
				else:  # expand the path
					for j in A[path[-1]]:
						new_list.append(path+[j])
			path_list = new_list
			print path_list
		return res

a = Solution()
dict = ["abc","a","ca","ab", "ad"]
str = "abcaad"
print a.wordBreak(str,dict)

