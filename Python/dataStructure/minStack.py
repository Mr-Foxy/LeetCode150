class MinStack:
	def __init__(self):
		self.l = []
		self.min_val = float('INF')
  # @param x, an integer
  # @return an integer
	def push(self, x):
		self.l.append(x)
		if x < self.min_val:
			self.min_val = x
		
  # @return nothing
	def pop(self):
		if self.l.pop() == self.min_val:
			min_v = float('INF')
			for i in range(len(self.l)):
				if self.l[i] < min_v:
					min_v = self.l[i]
			self.min_val = min_v
      
  # @return an integer
	def top(self):
		return self.l[-1]
      
  # @return an integer
	def getMin(self):
		return self.min_val
