#import pdb 
class Solution:
	# @param a list of integers
	# @return an integer
	def removeDuplicates(self, A):
		length = len(A)
		if length == 0 or length == 1:
			return length
		num = 1
		#pdb.set_trace()
		for i in range(1, length):
			if A[i] != A[i-1]:
				A[num] = A[i]
				num += 1
		return num

A = Solution()
t_str = [0,0,0,0,0]
print A.removeDuplicates(t_str)
print t_str

