class Solution:
	# @param num, a list of integer
	# @return an integer
	def longestConsecutive(self, num):
		if not num:
			return 0
		max_len = 1
		cur_len = 0
		l = dict()
		for i in num:
			l[i] = 1
		for i in num:
			cur_len = l.get(i)
			j = i + 1
			while l.get(j):
				cur_len += l.get(j)
				del l[j]
				j +=1
			l[i] = cur_len
			
			max_len = max(max_len, cur_len)
		return max_len
				
a = Solution()
print a.longestConsecutive([0])

