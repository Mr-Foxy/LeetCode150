# Definition for an interval.
class Interval:
	def __init__(self, s=0, e=0):
		self.start = s
		self.end = e

class Solution:
	# @param intervals, a list of Interval
	# @return a list of Interval
	def merge(self, intervals):
		intervals.sort(key=lambda interval: interval.start)
		i = 1
		l = len(intervals)
		while i < l: 
			
			if intervals[i].start <= intervals[i - 1].end:
				intervals[i - 1].end = max(intervals[i-1].end, intervals[i].end)
				del intervals[i]
				i -= 1
				l -= 1
			i += 1

		return intervals

test = []
interval4 = Interval(15,18)
test.append(interval4)
interval1 = Interval(1,3)
test.append(interval1)
interval3 = Interval(8,10)
test.append(interval3)
interval2 = Interval(2,6)
test.append(interval2)

A = Solution()
A.merge(test)
for i in test:
	print i.start, i.end


