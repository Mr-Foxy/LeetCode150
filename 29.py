class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
		if not prices:
			return 0
		history = [0] * len(prices)
		future = [0] * len(prices)
		valley = prices[0]
		peak = prices[-1]
		max_profit = 0
		for i in range(len(prices)):
			valley = min(valley, prices[i])
			if i > 0:
				history[i] = max(history[i-1], prices[i] - valley)

		for i in reversed(range(len(prices))):
			peak = max(peak, prices[i])
			if i < len(prices) - 1:
				future[i] = max(future[i+1], peak - prices[i])
			max_profit = max(max_profit, history[i] + future[i])

		print history
		print future
		return max_profit

a = Solution()
print a.maxProfit([3,2,6,5,0,3])
