import pdb
class Solution:
  # @param A, a list of integers
  # @param target, an integer to be inserted
  # @return integer
	def searchInsert(self, A, target):
		len_A = len(A)
		return self.searchInsert_AUX(A, 0, len_A - 1, target)

	def searchInsert_AUX(self, A, start, end, target):
		if start > end:
			return start
		mid = (start + end) / 2
		if target == A[mid]:
			return mid
		if target > A[mid]:
			return self.searchInsert_AUX(A, mid + 1, end, target)
		else:
			return self.searchInsert_AUX(A, start, mid - 1, target)
        
a = Solution()
print a.searchInsert([1,3,5,6], 4)
