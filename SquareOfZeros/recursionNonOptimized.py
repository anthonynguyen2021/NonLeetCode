# Time = O(N^4) | Space = O(N^3)
def squareOfZeroes(matrix):
	cache = {}
	n = len(matrix)
	
    topRow = 0
	bottomRow = n - 1
	
	leftCol = 0
	rightCol = n - 1
	return hasSquareOfZeros(matrix, topRow, bottomRow, leftCol, rightCol, cache)

def hasSquareOfZeros(matrix, r1, r2, c1, c2, cache):
	if r1 >= r2 or c1 >= c2:
		return False
	
	key = str(r1) + "-" + str(r2) + "-" + str(c1) + "-" + str(c2)
	if key in cache:
		return cache[key]
	
	cache[key] = (
		isSquareOfZeros(matrix, r1, r2, c1, c2) or
		hasSquareOfZeros(matrix, r1+1, r2, c1+1, c2, cache) or
		hasSquareOfZeros(matrix, r1+1, r2, c1, c2-1, cache) or
		hasSquareOfZeros(matrix, r1, r2-1, c1+1, c2, cache) or
		hasSquareOfZeros(matrix, r1, r2-1, c1, c2-1, cache) or
		hasSquareOfZeros(matrix, r1+1, r2-1, c1+1, c2-1, cache)
	
	)
	
	return cache[key]

def isSquareOfZeros(matrix, r1, r2, c1, c2):
	for row in range(r1, r2+1):
		if matrix[row][c1] != 0 or matrix[row][c2] != 0:
			return False
	for col in range(c1, c2+1):
		if matrix[r1][col] != 0 or matrix[r2][col] != 0:
			return False
	return True
	
