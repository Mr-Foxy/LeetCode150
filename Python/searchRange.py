class Solution
	# @param A, a list of integers
	# @param target, an integer to be searched
	# @return a list of length 2, [index1, index2]
	def searchRange(self, A, target):
		l = len(A)
		
		res_b1 = -1
		res_b2 = -1

		p = 0
		q = l - 1
		while p <= q:
			mid = (p + q) / 2
			if A[mid] == target:
				if mid == 0 or A[mid - 1] != target:
					res_b1 = mid
					break

			if A[mid] >= target:
				q = mid - 1
			else:
				p = mid + 1

		p = 0
		q = l - 1
		while p <= q:
			mid = (p + q) / 2
			if A[mid] == target:
				if mid == l - 1 or A[mid + 1] != target:
					res_b2 = mid
					break

			if A[mid] > target:
				q = mid - 1
			else:
				p = mid + 1
		
		return [res_b1, res_b2]

A = Solution()
print A.searchRange([1], 1)
		


