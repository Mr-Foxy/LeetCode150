import pdb
class Solution:
	# @return an integer
	def threeSumClosest(self, num, target):
		num.sort()
		min_v = 0x3f3f3f3f
		val_closest = -1
		l = len(num)
		i = 0
		end = False
		prev = -1
		# prev is:
		# default : -1 temp > target : 1 temp < target : 0
		# pdb.set_trace()
		while i < l - 2 and not end:
			j = i + 1
			k = l - 1
			while j < k:
				temp = num[i] + num[j] + num[k]
				if temp == target:
					min_v = 0
					val_closest = temp
					end = True
					break

				elif temp > target:
					if temp - target < min_v:
						val_closest = temp
						min_v = temp - target
					if prev == -1:
						prev = 1
					k -= 1

				else:
					if target - temp < min_v:
						val_closest = temp
						min_v = target - temp
					if prev == -1:
						prev = 0
					j += 1

			i += 1

		return val_closest

A = Solution()
print A.threeSumClosest([1,2,4,8,16,32,64,128], 82)
