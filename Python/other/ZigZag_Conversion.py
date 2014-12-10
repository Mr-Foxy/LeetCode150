import pdb
class Solution:
  # @return a string
  def convert(self, s, nRows):
		res = [[] for i in range(nRows)]
		cur = len(s)
		col = 0
		j = 0
		while cur > 2 * nRows - 2:
			#pdb.set_trace()
			for i in range(nRows):
				res[i].append(s[j])
				j += 1
				cur -= 1
			for i in range(1, nRows-1)[::-1]:
				res[i].append(s[j])
				j += 1
				cur -= 1

		if cur <= nRows:
			for i in range(cur):
				res[i].append(s[j])
				j += 1
		else:
			for i in range(nRows):
				res[i].append(s[j])
				j += 1
				cur -= 1
			#pdb.set_trace()
			for i in range(nRows-cur-1, nRows-1)[::-1]:
				res[i].append(s[j])
				j += 1
		res_str = ""
		for lst in res:
			res_str += ''.join(lst)
		return res_str

a = Solution()
print a.convert("ABCDEF", 4)
