class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
		one = 0
		two = 0
		three = 0
		for i in A:
			two |= i & one
			one = i ^ one
			three = one & two
			one &= ~three
			two &= ~three
		return one

list = [5,4,5,2,5,4,2,6,2,4]
a = Solution()
print a.singleNumber(list)
        
