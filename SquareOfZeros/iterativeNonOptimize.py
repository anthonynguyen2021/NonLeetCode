# Explanation of solution: The idea is to go through all of the entries of the matrix at index (i, j), and check for candidate squares whose upper left hand corner
# starts at index (i, j). From there, we look at square of size 2, ..., and so on until it's out of bounds - see while loop.

# Explanation of complexities: Time comes from the two for loops which is O(n^2). The while loop will look at squares whose upper left hand corner is at index topRow and leftCol and increase the
# size of squares until out of bounds, so this is O(n). Checking if the square has boundary of zeros, this is O(n) using a for-loop.

# Time = O(N^4) | Space = O(1) where N = len(matrix)
def squareOfZeroes(matrix):

	n = len(matrix)

	for topRow in range(0, n):
		for leftCol in range(0, n):

			squareLength = 2

			while topRow + (squareLength - 1) < n and leftCol + (squareLength - 1) < n:

				bottomRow = topRow + (squareLength - 1)
				rightCol = leftCol + (squareLength - 1)

				if isSquareOfZeros(matrix, topRow, bottomRow, leftCol, rightCol):
					return True
				squareLength += 1

	return False


def isSquareOfZeros(matrix, r1, r2, c1, c2):

	for row in range(r1, r2 + 1):
		if matrix[row][c1] != 0 or matrix[row][c2] != 0:
			return False

	for col in range(c1, c2 + 1):
		if matrix[r1][col] != 0 or matrix[r2][col] != 0:
			return False

	return True
