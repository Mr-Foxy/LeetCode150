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
		
		cur = 0
		profit = 0
		max_profit = 0
		for i in variance:
			if i < 0 and profit == 0:
				continue
			profit += i
			if profit < 0:
				profit = 0
			max_profit = max(profit, max_profit)
		return max_profit

a = Solution()
print a.maxProfit([6,1,3,2,4,7])
