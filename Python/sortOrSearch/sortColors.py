class Solution:
  # @param A a list of integers
  # @return nothing, sort in place
  def sortColors(self, A):
		i = 0

		for k in range(3):
			for j in range(i, len(A)):
				if A[j] == k:
					A[j], A[i] = A[i], A[j]
					i += 1

A = Solution()
test = []
A.sortColors(test)
print test

