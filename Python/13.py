import pdb
class Solution:
	# @param s, a string
	# @param dict, a set of string
	# @return a boolean
	def wordBreak(self, s, dict):
		n = len(s) 
		table = [[ 0 for i in range(n)] for j in range(n)]

		pdb.set_trace()
		for l in range(1, n + 1):
			for i in range(0, n - l + 1):
				j = i + l - 1
				q = False
				for k in range(i, j - 1 + 1):
					q = q or ( table[i][k] and table[k+1][j] )
				if q == False:
					tmp = s[i : j+1]
					for words in dict:
						if words == tmp:
							q = True

				table[i][j] = q

		return table[0][len(s) - 1]


def main():
	dict = ["a"]
	str = "a"
	a = Solution()
	if a.wordBreak(str,dict):
		print "WoW"
	else:
		print "ehhh"
if __name__ == '__main__':
	main()
			
