class Solution:
	# @return a string
	def countAndSay(self, n):
		cur = "1"
		
		next_str = ""
		old = None
		times = 0
		for j in range(1, n):
			for i in range(len(cur)):
				if not old:
					old = cur[i]
					times = 1
					continue
				if cur[i] == old:
					times += 1
				else:
					next_str += str(times)
					next_str += old
					old = cur[i]
					times = 1

			if times > 0:
				next_str += str(times)
				next_str += old
			times = 0
			old = None

			cur = next_str
			next_str = ""

		return cur

A = Solution()
print A.countAndSay(2)
