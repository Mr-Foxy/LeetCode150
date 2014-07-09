class Solution:
	# @param s, a string
	# @return a string
	def reverseWords(self, s):
		j = 0
		result = ""
		temp_word = ""
		for i in range(len(s)):
			temp_word[j++] = s[i]
			# cache character
			if s[i] == " ":
				for k in range(len(temp_word)):
					
				temp_word = ""
				# put word in new string
				

