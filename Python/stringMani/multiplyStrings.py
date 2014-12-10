class Solution:
	# @param num1, a string
	# @param num2, a string
	# @return a string
	def multiply(self, num1, num2):
		l1 = len(num1)
		l2 = len(num2)

		res = [0 for i in range(l1 + l2)] 

		for i in (range(l1)):
			carry = 0
			for j in (range(l2)):
				val = int(num1[l1 - 1 - i]) * int(num2[l2 - 1 - j]) + carry + res[i+j]
				carry = val / 10
				val = val % 10
				res[i+j] = val
			if carry > 0:
				res[l2 + i] += carry
		
		i = l1 + l2 - 1
		while res[i] == 0 and i >= 0:
			i -= 1
		
		if i == -1:
			return "0"

		resStr = ""
		while i >= 0:
			resStr = resStr + str(res[i])
			i -= 1
				
		return resStr
	
A = Solution()
print A.multiply("99", "99")
