class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
		if not dict:
			return 0
		char = "abcdefghijklmnopqrstuvwxyz"
		queue = [[start, 1]]
		dist = set(start)
		while len(queue):
			word, dis = queue.pop(0)
			dis += 1
			for j in char:
				for k in range(len(word)):
					tmp = word[:k] + j + word[k+1:]
					if tmp == end:
						return dis
					if tmp in dict and tmp not in dist:
						queue.append([tmp, dis])
						dist.add(tmp)
		return 0

a = Solution()
start = "qa"
end = "sq"
dict = ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]
print a.ladderLength(start, end, dict)
