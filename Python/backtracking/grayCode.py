import pdb
class Solution:
  # @return a list of integers
	def grayCode(self, n):
		first_str = []
		res = []
		for i in range(n):
			first_str += '0'
		
		queue = [(first_str, 0)]
		
		while queue:
			#pdb.set_trace
			cur = queue.pop(0)
			res.append(self.transToInt(cur[0]))
			cur_n = cur[1]
			while cur_n < n:
				cur_l = list(cur[0])
				cur_l[cur_n] = "1"
				cur_n += 1
				queue.append((cur_l, cur_n))

		return res

	def transToInt(self, l):
		num = 0
		for i in range(len(l)):
			num += int(l[i]) * pow(2, i)

		return num

A = Solution()
print A.grayCode(2)
