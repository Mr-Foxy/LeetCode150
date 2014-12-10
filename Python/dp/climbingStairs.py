class Solution:
  # @param n, an integer
  # @return an integer
  def climbStairs(self, n):
		l = [0 for i in range(n)]
		if n == 0:
			return 0
		if n == 1:
			return 1
		if n == 2:
			return 2

		l[0] = 1
		l[1] = 2
		for i in range(2, n):
			l[i] = l[i-1] + l[i-2]
			
		return l[n-1]

a = Solution()
print a.climbStairs(5)
			
        
