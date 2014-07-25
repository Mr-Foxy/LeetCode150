class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
		char = [chr(i) for i in range(97,123)]
		queue = []
		if not dict:
			return 0
		length = 1
		queue.append([start])
		if start in dict:
			dict.remove(start)
		res = []
		is_answered = False
		while queue:
			queue_size = len(queue)
			for i in range(queue_size):
				current = queue[0][-1]
				for j in char:
					for k in range(len(current)):
						tmp = current[:k] + j + current[k+1:]
						if tmp == end:
							queue.append(queue[0] + [end])
						elif tmp in dict and not tmp in queue[0]:
							queue.append(queue[0] + [tmp])
				del queue[0]
			for list in queue:
				if list[-1] == end:
					res.append(list)
					is_answered = True
			if is_answered:
				return res
		return 0

a = Solution()
start = "hit"
end = "cog"
dict = ["hot", "dot", "dog", "lot", "log"]
print a.ladderLength(start,end,dict)
