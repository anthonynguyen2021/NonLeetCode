# Idea Solution: 

# Time = O(1) | Space = O(1)
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
	
	return solvePartialSudoku(row, col+1, board)

def putDigits(row, col, board):
	for digit in range(1, 10):
		if validation(digit, row, col, board):
			board[row][col] = digit
			if solvePartialSudoku(row, col+1, board):
				return True
	board[row][col] = 0
	return False


def validation(value, row, col, board):
	# Check if value is not in a given row
	if value in board[row]:
		return False
	# Check if value is not in column
	elif value in map(lambda r : r[col], board):
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
