import pdb
class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
	def solve(self, board):
		longth = len(board)
		if longth == 0:
			return board
		width = len(board[0])
		t = []
		line = []
		for i in range(1, longth - 1):
			for j in range(1, width - 1):
				if board[i][j] == 'O' and not (i, j) in t:
					line, is_change = self.detect_sur(board, i, j)
					if is_change:
						for coor in line:
							board[coor[0]][coor[1]]= 'X'
					t += line
	
	def detect_sur(self, board, i, j):
		line = []
		line.append((i,j))
		is_change = self.detect_sur_aux(board, 0, i, j, line)
		return line, is_change

	def detect_sur_aux(self, board, dir, i, j, line):
		result = True
		if i == 0 or i == len(board) - 1 or j == 0 or j == len(board[0]) - 1:
			return False
		if (i, j) in line:
			return True
		# Check up
		if board[i][j-1] == 'O' and dir != 1:
			line.append((i, j-1))
			result &= self.detect_sur_aux(board, 2, i, j-1, line)

		# Check down
		if board[i][j-1] == 'O' and dir != 2:
			line.append((i, j+1))
			result &= self.detect_sur_aux(board, 1, i, j+1, line)

		# Check left
		if board[i-1][j] == 'O' and dir != 3:
			line.append((i-1, j))
			result &= self.detect_sur_aux(board, 4, i-1, j, line)

		# Check right
		if board[i+1][j] == 'O' and dir != 4:
			line.append((i+1, j))
			result &= self.detect_sur_aux(board, 3, i+1, j, line)
	
		return result
		
def str_to_array(a):
	board = []
	for s in a:
		new = []
		for c in s:
			new.append(c)
		board.append(new)
	return board

board = str_to_array(["OXOOOOOOO","OOOXOOOOX","OXOXOOOOX","OOOOXOOOO","XOOOOOOOX","XXOOXOXOX","OOOXOOOOO","OOOXOOOOO","OOOOOXXOO"])
#board = str_to_array(["OOO","OOO","OOO"])
a = Solution()
a.solve(board)
pdb.set_trace()
