class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
		result = 0
		for i in A:
			result ^= i
		return result


A = [1,1,2,2,5,4,5,6,4]
a = Solution()
print a.singleNumber(A)
        
