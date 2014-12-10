class Solution:
  # @param s, a string
  # @return an integer
  def numDecodings(self, s):
		if not s:
			return 0

		num = [0, 0]
		for i in s:
			n = int(i)
			num.append(int(i))

		l = len(num)

		dp = [0 for i in range(l)]
		
		dp[0] = 1
		dp[1] = 1

		for i in range(2, l):
			cur_dp = 0
			cur_n = num[i]
			if cur_n >= 1 and cur_n <= 9:
				cur_dp += dp[i-1]
			cur_n = num[i - 1] * 10 + num[i]
			if cur_n >= 10 and cur_n <= 26:
				cur_dp += dp[i-2]
			if cur_dp == 0:
				return 0
			dp[i] = cur_dp

		return dp[l - 1]

A = Solution()
print A.numDecodings("")
        
