import pdb
class Solution:
	# @param num, a list of integer
	# @return an integer
	def findMin(self, num):
		l = len(num)
		p = 0
		q = l - 1

		while True:
			#pdb.set_trace()
			curIndex = (q + p) / 2
			curN = num[curIndex]
			if p == q or (curN < num[curIndex + 1] and curN < num[curIndex - 1]):
				return curN
			if num[curIndex] >= num[p] and num[curIndex] <= num[q]:
				return num[p]
			if num[curIndex] <= num[p] and num[curIndex] <= num[q]:
				q = curIndex - 1
			if num[curIndex] >= num[p] and num[curIndex] >= num[q]:
				p = curIndex + 1
		
A = Solution()
test = [2,1]
print A.findMin(test)

