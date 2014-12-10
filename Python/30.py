class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
		if not prices:
			return 0
		variance = prices
		i = len(variance) - 1
		while i >= 1:
			variance[i] = variance[i] - variance[i-1]
			i -= 1
		variance[0] = 0

		res = 0
		for i in variance:
			res += i if i > 0 else 0

		return res

a = Solution()
print a.maxProfit([6,1,3,2,4,7])
        
