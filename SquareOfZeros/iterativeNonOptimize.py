# Time = O(N^4) | Space = O(1)
def squareOfZeroes(matrix):
	n = len(matrix)
    for topRow in range(0, n):
		for leftCol in range(0, n):
			squareLength = 2
			while topRow + (squareLength-1) < n and leftCol + (squareLength-1) < n:
				bottomRow = topRow + (squareLength-1)
				rightCol = leftCol + (squareLength-1)
				if isSquareOfZeros(matrix, topRow, bottomRow, leftCol, rightCol):
					return True
				squareLength += 1
	return False

def isSquareOfZeros(matrix, r1, r2, c1, c2):
	for row in range(r1, r2+1):
		if matrix[row][c1] != 0 or matrix[row][c2] != 0:
			return False
	for col in range(c1, c2+1):
		if matrix[r1][col] != 0 or matrix[r2][col] != 0:
			return False
	return True
