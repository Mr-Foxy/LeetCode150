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

			if carry > 0:
				res[
				
		return res
	
#	def add(self, num1, num2):
#		if len(num1) < len(num2):
#			return self.add(num2, num1)
#
#		l1 = len(num1)
#		l2 = len(num2)
#		res = ""
#		
#		p1 = l1 - 1
#		p2 = l2 - 1
#
#		forward = 0
#		while p2 >= 0:
#			val = int(num1[p1]) + int(num2[p2]) + forward
#			forward = 0
#
#			if val >= 10:
#				forward = 1
#				val = val % 10
#
#			res = str(val) + res
#
#			p1 -= 1
#			p2 -= 1
#		
#		while p1 >= 0:
#			val = int(num1[p1]) + forward
#			forward = 0
#		
#			if val >= 10:
#				forward = 1
#				val = val % 10
#		
#			res = str(val) + res
#			p1 -= 1
#
#		return res
			
A = Solution()
print A.multiply("99", "99")
#print A.add("81", "810")
