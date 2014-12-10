class Solution:
    # @param digits, a list of intteger digits
    # @return a list of integer digits
    def plusOne(self, digits):
		l = len(digits)

		carry = 0
		first = 1
		for i in reversed(range(l)):
			val = digits[i] + carry + first
			first = 0
			carry = val / 10
			val = val % 10
			digits[i] = val

		if carry == 1:
			digits = [1] + digits

		return digits

A = Solution()
print A.plusOne([9,9,9])
