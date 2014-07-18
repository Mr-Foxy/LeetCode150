class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
		basin = []
		peak = []
		candy = [0] * len(ratings)
		length = len(ratings)
		for i in range(length):
			if i > 0 and i < length - 1:
				if ratings[i] < ratings[i - 1] and ratings[i] < ratings[i+1]:
					basin.append(i)
			elif i == 0:
				if ratings[i] < ratings[i + 1]:
					basin.append(i)
			elif i == length - 1:
				if ratings[i] < ratings[i - 1]:
					basin.append(i)

			if i > 0 and i < length - 1:
				if ratings[i] > ratings[i - 1] and ratings[i] > ratings[i+1]:
					peak.append(i)
			elif i == 0:
				if ratings[i] > ratings[i + 1]:
					peak.append(i)
			elif i == length - 1:
				if ratings[i] > ratings[i - 1]:
					peak.append(i)
		print basin
		print peak

		j = 0
		for i in range(len(basin)):
			if basin[i] > peak[j]:
				candy_num = 1
				k = basin[i]
				while k > peak[j] and k > 0:
					print k
					candy[k] = candy_num
					candy_num += 1
					k -= 1

				if candy_num > candy[peak[j]]:
					candy[peak[j]] = candy_num
				
				if j == len(peak) - 1:
					break

				candy_num = 1
				k = basin[i]
				while k < peak[j + 1] and k < length:
					candy[k] = candy_num
					candy_num += 1
					k += 1

				if candy_num > candy[peak[j + 1]]:
					candy[peak[j + 1]] = candy_num

		return candy

list = [7,4,6,8,7,4,2,9,10,15,5]
a = Solution()
print a.candy(list)
