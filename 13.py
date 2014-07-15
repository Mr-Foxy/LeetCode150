class Solution:
	# @param s, a string
	# @param dict, a set of string
	# @return a boolean
	def wordBreak(self, s, dict):
		result = False
		if s == "":
			return True
		tmp = ""
		for i in range(len(s)):
			tmp += s[i]
			for words in dict:
				if words == tmp:
					result = self.wordBreak(s[i+1:],dict)
					break
		return False or result


def main():
	dict = ["aaaa", "aaa"]
	str = "aaaaaaa"
	a = Solution()
	if a.wordBreak(str,dict):
		print "WoW"
	else:
		print "ehhh"
if __name__ == '__main__':
	main()
			
