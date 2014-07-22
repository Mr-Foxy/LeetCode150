import pdb
class Solution:
	# @param gas, a list of integers
	# @param cost, a list of integers
	# @return an integer
	def canCompleteCircuit(self, gas, cost):
		gas_left = gas_needed = start = 0
		for i, (g, c) in enumerate(zip(gas,cost)):
			gas_left += g - c
			if gas_left < 0:
				#pdb.set_trace()
				gas_needed -= gas_left
				start = i + 1
				gas_left = 0

		return start if gas_left >= gas_needed else -1
			
		# My Brute Force Solution
		'''
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
		'''
a = Solution()
test_gas = [1,2]
test_cost = [2,1]
print a.canCompleteCircuit(test_gas, test_cost)
