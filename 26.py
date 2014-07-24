class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
		queue = []
		if not dict:
			return 0
		length = 1
		queue.append([start])
		if start in dict:
			dict.remove(start)
		while queue:
			queue_size = len(queue)
			n = 0
			for i in range(queue_size):
				current = queue[n][-1]
				is_changed = False
				for j in "abcdefghijklmnopqrstuvwxyz":
					for k in range(len(current)):
						tmp = current[:k] + j + current[k+1:]
						print tmp
						if tmp == end:
							return length + 1
						if tmp in dict:
							queue[n].append(tmp)
							is_changed = True
				if is_changed:
					n += 1
				else:
					del queue[n]
			length += 1
		return 0

a = Solution()
start = "hit"
end = "cog"
dict = ["hot", "dot", "dog", "lot", "log"]
print a.ladderLength(start,end,dict)
