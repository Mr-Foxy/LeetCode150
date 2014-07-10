class Solution:
	# @param s, a string
	# @return a string
	def reverseWords(self, s):
		first = True
		repeat = False
		j = 0
		result = ""
		temp_word = ""
		s = s.strip()
		if s == "":
			return result
		for i in s:
			# cache character
			if i == " ":
				if repeat:
					continue
				# put word in new string
				if first:
					result = temp_word + result	
					first = False
				else:
					result = temp_word + " " + result	
				temp_word = ""
				repeat = True
			else:
				repeat = False
				temp_word += i

		if first:
			result = temp_word + result	
		else:
			result = temp_word + " " + result	
		return result

def test():
	a = Solution()
	print a.reverseWords("the sky is blue") + "#"
	print a.reverseWords("     ") + "#"
	print a.reverseWords("a") + "#"

if __name__ == '__main__':
	test()

				

