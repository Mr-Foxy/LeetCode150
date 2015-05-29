class Solution:
	# @param tokens, a list of string
	# @return an integer
	def evalRPN(self, tokens):
		stack = []
		for i in tokens:
			if i in ["+", "-", "*", "/"]:
				right = stack.pop()
				left = stack.pop()
				if i == "+":
					result = left + right 
				if i == "-":
					result = left - right 
				if i == "*":
					result = left * right 
				if i == "/":
					result = int(float(left) / right)
				stack.append(result)
			else:
				value = int(i)
				stack.append(value)
		return stack.pop()

def main():
	a = Solution()
	print a.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
if __name__ == '__main__':
	main()
