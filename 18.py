import pdb
class Solution:
	# @param gas, a list of integers
	# @param cost, a list of integers
	# @return an integer
	def canCompleteCircuit(self, gas, cost):
		variance = [i - j for i, j in zip(gas, cost)]
		print variance
		null = False
		for i in range(len(variance)):
			if variance[i] < 0:
				continue

			cur_tank = variance[i]
			#pdb.set_trace()
			for j in range(i + 1, len(variance)):
				cur_tank += variance[j]
				if cur_tank < 0:
					null = True

			if null:
				null = False
				continue

			for j in range(0, i):
				cur_tank += variance[j]
				if cur_tank < 0:
					null = True

			if null:
				null = False
				continue

			return i
		
		return -1

a = Solution()
test_gas = [2,2,6]
test_cost = [1,5,1]
print a.canCompleteCircuit(test_gas, test_cost)
