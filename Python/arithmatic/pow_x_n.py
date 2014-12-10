class Solution:
  # @param x, a float
  # @param n, a integer
  def pow(self, x, n):
		if n < 0:
			n = -1 * n
			x = 1 / x

		cur = n
		res = 1

		f = x
		while cur > 0:
			if cur % 2 == 1:
				res = res * f
			f = f * f
			cur = cur >> 1
		
		return res

a = Solution()
print a.pow(3.3, 2)
#print a.pow(0.00001,2147483647)
        
