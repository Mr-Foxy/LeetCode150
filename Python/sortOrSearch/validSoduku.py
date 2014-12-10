class Solution:
	# @param board, a 9x9 2D array
	# @return a boolean
	def isValidSudoku(self, board):
		num_l = range(1, 10)
		queue = []
		size = len(board)

		for i in range(size):
			for j in range(size):
				if board[i][j] == '.':
					new_list = []
					for k in num_l:
						if queue:
							for p in queue
								if valid_row(p, board, k) and valid_col(board, k) and valid_block(board, k):
