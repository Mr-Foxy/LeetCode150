class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
		prev = None
		len_l = len(triangle)
		for i in range(len_l):
			tmp = triangle[i]
			if prev:
				len_prev = len(prev)
				for j in range(1,len_prev):
					tmp[j] = tmp[j] + min(prev[j], prev[j-1])
				tmp[0] = tmp[0] + prev[0]
				tmp[-1] = tmp[-1] + prev[-1]
			prev = tmp
			#print tmp
		return min(tmp)

#a = Solution()
#test = []
#test.append([-1])
#test.append([3,2])
#test.append([-3,1,-1])
#test.append([4,1,8,3])
#print a.minimumTotal(test)
