import pdb
class Solution:
	# @param A, a list of integers
	# @param target, an integer to be searched
	# @return an integer
	def search(self, A, target):
		return self.search_AUX(A, target, 0, len(A) - 1)
	def search_AUX(self, A, target, low, high):
		if low > high:
			return -1
		mid = ( low + high ) / 2
		if A[mid] == target:
			return mid
		if A[low] <= A[mid]:
			if target >= A[low] and target < A[mid]:
				return self.search_AUX(A, target, low, mid)
			else:
				return self.search_AUX(A, target, mid+1, high)

		if A[mid] < A[high]:
			if target > A[mid] and target <= A[high]:
				return self.search_AUX(A, target, mid+1, high)
			else:
				return self.search_AUX(A, target, low, mid)

		return -1
					

a = Solution()
A = [1,3]
q = 3
print a.search(A, q)
