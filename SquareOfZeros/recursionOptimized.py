# Time = O(N^3) | Space = O(N^3)
def squareOfZeroes(matrix):
	infoMatrix = preComputeNumberOfZeros(matrix)
	cache = {}
	n = len(matrix)
	
    	topRow = 0
	bottomRow = n - 1
	
	leftCol = 0
	rightCol = n - 1
	return hasSquareOfZeros(infoMatrix, topRow, bottomRow, leftCol, rightCol, cache)

def hasSquareOfZeros(infoMatrix, r1, r2, c1, c2, cache):
	if r1 >= r2 or c1 >= c2:
		return False
	
	key = str(r1) + "-" + str(r2) + "-" + str(c1) + "-" + str(c2)
	if key in cache:
		return cache[key]
	
	cache[key] = (
		isSquareOfZeros(infoMatrix, r1, r2, c1, c2) or
		hasSquareOfZeros(infoMatrix, r1+1, r2, c1+1, c2, cache) or
		hasSquareOfZeros(infoMatrix, r1+1, r2, c1, c2-1, cache) or
		hasSquareOfZeros(infoMatrix, r1, r2-1, c1+1, c2, cache) or
		hasSquareOfZeros(infoMatrix, r1, r2-1, c1, c2-1, cache) or
		hasSquareOfZeros(infoMatrix, r1+1, r2-1, c1+1, c2-1, cache)
	
	)
	
	return cache[key]

def preComputeNumberOfZeros(matrix):
	infoMatrix = [[x for x in row] for row in matrix]
	
	n = len(infoMatrix)
	for row in range(n):
		for col in range(n):
			numZeros = 1 if matrix[row][col] == 0 else 0
			infoMatrix[row][col] = {"numZerosRight": numZeros, "numZerosBelow": numZeros}
	
	for row in reversed(range(n)):
		for col in reversed(range(n)):
			if matrix[row][col] == 1:
				continue
			if row < n-1:
				infoMatrix[row][col]["numZerosBelow"] += infoMatrix[row+1][col]["numZerosBelow"]
			if col < n-1:
				infoMatrix[row][col]["numZerosRight"] += infoMatrix[row][col+1]["numZerosRight"]
	return infoMatrix

def isSquareOfZeros(infoMatrix, r1, r2, c1, c2):
	lengthSquare = r2 - r1 + 1
	topBorder = infoMatrix[r1][c1]["numZerosRight"] >= lengthSquare
	leftBorder = infoMatrix[r1][c1]["numZerosBelow"] >= lengthSquare
	rightBorder = infoMatrix[r1][c2]["numZerosBelow"] >= lengthSquare
	bottomBorder = infoMatrix[r2][c1]["numZerosRight"] >= lengthSquare
	return topBorder and leftBorder and rightBorder and bottomBorder
