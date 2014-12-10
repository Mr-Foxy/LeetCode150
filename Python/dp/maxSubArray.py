class Solution:
# @param A, a list of integers
# @return an integer
	def maxSubArray(self, A):
		if not A:
			return []
		max_v = A[0]
		cur = A[0]
		for i in range(1, len(A)):
			if cur < 0:
				cur = 0
			cur += A[i]
			if cur > max_v:
				max_v = cur
		return max_v

A = Solution()
print A.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])

