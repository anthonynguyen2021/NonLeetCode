# Idea Solution: The idea is to use backtracking. We solve the sudoku board from row1 from left to right. Then go to row 2, from left to right, and so on. At each 0's we see, 
# We put a digit {1, 2, ... , 9} in that position (make sure it's valid) and call the function on the next spot. This function returns a bool meaning if we can solve it
# at the current row and column. 
# To understand the recursive nature of the solution, assume we're at (row, col) and we have solved the board correctly so far. Suppose at board[row][col], we have 0. 
# If we place a 1 there, we call the recursive function at index row, col+1. If we can't solve it, return False. Otherwise, return True. However if we can't solve it at
# (row, col) with 1 there, we check 2 and call the recursive function at index row, col+1 again. 


# Time = O(1) | Space = O(1) - the board is always a 9x9 so the amount of computation is always the same. The only additional storage is through the call stack, which is always
# constant. 
def solveSudoku(board):
	solvePartialSudoku(0, 0, board)
	return board


def solvePartialSudoku(row, col, board):
	
	if col == len(board[row]):
		row += 1
		col = 0
		if row == len(board):
			return True
	
	if board[row][col] == 0:
		return putDigits(row, col, board)
	
	return solvePartialSudoku(row, col + 1, board)


def putDigits(row, col, board):

	for digit in range(1, 10):

		if validation(digit, row, col, board):
			board[row][col] = digit
			if solvePartialSudoku(row, col + 1, board):
				return True

	board[row][col] = 0
	return False


def validation(value, row, col, board):
	# Check if value is not in a given row
	if value in board[row]:
		return False
	# Check if value is not in column
	elif value in map(lambda r: r[col], board):
		return False

	# Check if value is not in the subsquare
	subgridRowIdx = (row // 3) * 3
	subgridColIdx = (col // 3) * 3

	for rowIdx in range(3):
		for colIdx in range(3):

			rowToCheck = subgridRowIdx + rowIdx
			colToCheck = subgridColIdx + colIdx
			if value == board[rowToCheck][colToCheck]:
				return False

	# value is valid
	return True
