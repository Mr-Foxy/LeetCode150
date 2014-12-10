class Solution:
	# @param num, a list of integer
	# @return an integer
	def findPeakElement(self, num):
		l_num = len(num)

		if l_num == 1:
			return 0

		p = 0
		q = l_num - 1
		while True:
			mid = (p + q) / 2
			if (mid == l_num - 1 and num[mid-1] < num[mid]) or (mid == 0 and num[mid+1] < num[0]):
				return mid

			if num[mid - 1] < num[mid] and num[mid] > num[mid + 1]:
				return mid

			if num[mid] < num[mid + 1]:
				p = mid + 1
			elif num[mid] < num[mid - 1]:
				q = mid - 1

A = Solution()
print A.findPeakElement([1])

