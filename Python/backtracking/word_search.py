import pdb
class Solution:
	# @param board, a list of lists of 1 length string
	# @param word, a string
	# @return a boolean
	def inboard(self, board, i, j):
		length = len(board)
		width = len(board[0])
		return i >= 0 and i < length and j >=0 and j < width

	def exist(self, board, word):
		length = len(board)
		width = len(board[0])

		if length == 0 or width == 0:
			return False

		used = []  
		for i in range(length):
			used.append([False for k in range(width)])

		for i in range(length):
			for j in range(width):
				if (self.DFS(board, word, used, i, j, 0)):
					return True

		return False

	def DFS(self, board, word, used, i, j, n):
		if n == len(word):
			return True
		if self.inboard(board, i, j):
			if not used[i][j] and word[n] == board[i][j]:
				used[i][j] = True
				ret = False
				if self.DFS(board, word, used ,i-1, j, n+1):
					return True
				if self.DFS(board, word, used ,i+1, j, n+1):
					return True
				if self.DFS(board, word, used ,i, j+1, n+1):
					return True
				if self.DFS(board, word, used ,i, j-1, n+1):
					return True
				used[i][j] = False
				
		return False

a = Solution()
board = ["ABCE"]
board.append("SFCS")
board.append("ADEE")
print a.exist(board, "ABCCED")
