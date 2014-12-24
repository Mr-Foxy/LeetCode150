class Solution:
	# @return an integer
	def maxArea(self, height):
		p = 0
		q = len(height) - 1
		mx = 0
		
		while p < q:
			mx = max(min(height[p], height[q]) * (q - p), mx)
			
			if height[p] < height[q]:
				p += 1
			else:
				q -= 1

		return mx
