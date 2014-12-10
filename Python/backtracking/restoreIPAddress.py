class Solution:
	'''
	My face now:
	*_*
	'''
	def __init__(self):
		self.res = []
	# @param s, a string
	# @return a list of strings
	def restoreIpAddresses(self, s):
		self.restoreIpAddresses_AUX(0, [], s)
		return self.res
	
	def restoreIpAddresses_AUX(self, index, cur, s):
		
		if index >= len(s):
			if len(cur) == 4:
				self.res.append('.'.join(cur))
			return 

		cur_str = s[index]

		if len(cur) < 4:
			cur.append("" + cur_str)
			self.restoreIpAddresses_AUX(index + 1, cur, s)
			cur.pop()

		if cur:
			if cur[-1] == '0':
				return 
			cur[-1] += cur_str
			if int(cur[-1]) >= 0 and int(cur[-1]) <= 255:
				self.restoreIpAddresses_AUX(index + 1, cur, s)
			cur[-1] = cur[-1][:-1]


A = Solution()
print A.restoreIpAddresses("0000")
