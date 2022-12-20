# Explanation of solution: The idea is to build this matrix where at index (i, j), it'll tell us how many zeros below and to the right (including index (i, j)) until
# we see a 1. To build this, start with a matrix of the same size as 'matrix' and when we see a 0, add numZerosBelow, numZerosRight to be 1. Otherwise, set it to 1.
# We build this matrix from last row going backward to first row and from right column all the way backward to first column. At index (i, j), we see that if it
# corresponds to matrix[i][j] == 1, continue. Otherwise, we add numZerosBelow at index (i+1, j) to index (i, j) in infoMatrix and add numZerosRight at index (i, j+1) to 
# index (i, j) in infoMatrix provided we can access them (not last row or last column). Once we build this matrix, to check if a square has boundary zeros at key
# 'r1-r2-c1-c2', we look if infoMatrix[r1][c1]["numZerosBelow"] & infoMatrix[r1][c1]["numZerosRight"] are at least as great as the length of the square. We do the same
# for infoMatrix[r1][c2]["numZerosBelow"] & infoMatrix[r2][c1]["numZerosRight"] are at least as great as the length of the square.

# Explanation: It's the same as the recursive method (non-Optimize) but checking the boundaries are now O(1) given we have access to number of zeros below and to the right
# for each index (i, j). Note when we say number of zeros, we mean including the index (i, j) themselves and how many zeros to the right of (i, j) until we see a 1. Same
# logic with bottom.
# Time = O(N^3) | Space = O(N^3) where N = len(matrix)
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
		hasSquareOfZeros(infoMatrix, r1 + 1, r2, c1 + 1, c2, cache) or
		hasSquareOfZeros(infoMatrix, r1 + 1, r2, c1, c2 - 1, cache) or
		hasSquareOfZeros(infoMatrix, r1, r2 - 1, c1 + 1, c2, cache) or
		hasSquareOfZeros(infoMatrix, r1, r2 - 1, c1, c2 - 1, cache) or
		hasSquareOfZeros(infoMatrix, r1 + 1, r2 - 1, c1 + 1, c2 - 1, cache)
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
			if row < n - 1:
				infoMatrix[row][col]["numZerosBelow"] += infoMatrix[row+1][col]["numZerosBelow"]
			if col < n - 1:
				infoMatrix[row][col]["numZerosRight"] += infoMatrix[row][col+1]["numZerosRight"]

	return infoMatrix


def isSquareOfZeros(infoMatrix, r1, r2, c1, c2):

	lengthSquare = r2 - r1 + 1
	topBorder = infoMatrix[r1][c1]["numZerosRight"] >= lengthSquare
	leftBorder = infoMatrix[r1][c1]["numZerosBelow"] >= lengthSquare
	rightBorder = infoMatrix[r1][c2]["numZerosBelow"] >= lengthSquare
	bottomBorder = infoMatrix[r2][c1]["numZerosRight"] >= lengthSquare

	return topBorder and leftBorder and rightBorder and bottomBorder
