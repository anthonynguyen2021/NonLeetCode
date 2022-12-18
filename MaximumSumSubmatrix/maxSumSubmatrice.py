

def maximumSumSubmatrix(matrix, size):
	'''
	Brute force idea:
 
	Similar to the nested forloop in the main function, we sum of the elements of the squares, so the time complexity is O(w * h * size * size) with O(1) space.

	Explanation of solution:

	If we have a matrix called sumsMatrix such that sumsMatrix[i][j] will sum all elements in matrix[:i+1][:j+1] (not Python notation), we can
	compute all of the square submatrices sum in O(1) time. To create sumsMatrix, we first initialize sumsMatrix[0][0] = matrix[0][0]. For the first row,
	we set sumsMatrix[0][j] = sumsMatrix[0][j-1] + matrix[0][j] and the first column as sumsMatrix[i][0] = sumsMatrix[i-1][0] + matrix[i][0]. To populate the non-left/top wall
	of the matrix, we set sumsMatrix[i][j] = matrix[i][j] + sumsMatrix[i][j-1] + sumsMatrix[i-1][j] - sumsMatrix[i-1][j-1] (draw a picture to see). Now to the main function,
	if our square doesn't touch the left and top wall, we have our formula will do the following for the sum of the square: sumsMatrix[row][col] - sumsMatrix[row][col - size] 
	- sumsMatrix[row - size][col] + sumsMatrix[row - size][col - size] (draw a picture to see). Note that if the square we're considering touches the left wall and not the top wall, 
	we have the following formula for the square: sumsMatrix[row][col] - sumsMatrix[row - size][col]. If our square touches the top but not the left wall, the sum of the
	square elements is sumsMatrix[row][col] - sumsMatrix[row][col - size]. If our square touches the left AND top wall, the sum of the squares is just sumsMatrix[row][col]. Note
	that the squares we're considering will have bottom right hand corner index (row, col) in Python indexing - see code below.

	Explanation of complexities:

	The matrix sumsMatrix is build using O(w * h) space. For time, it takes O(w * h) to build sumsMatrix. Worst case, we might have O(w * h) square 
	submatrices. But the nested loop is approximately O(w * h) where the work inside is O(1).

	Time: O(w * h) where w is the width and h is the height
	Space: O(w * h)
	'''
	sumsMatrix = getTotalSumMatrix(matrix)
	maxSumSeen = float('-inf')

	for row in range(size - 1, len(matrix)):
		for col in range(size - 1, len(matrix[row])):

			totalSumSubmatrix = sumsMatrix[row][col]
			touchesTopBorder = row == (size - 1)

			if not touchesTopBorder:
				totalSumSubmatrix -= sumsMatrix[row - size][col]
		
			touchesLeftBorder = col == (size - 1)

			if not touchesLeftBorder:
				totalSumSubmatrix -= sumsMatrix[row][col - size]
		
			notTouchingLeftAndTop = not touchesLeftBorder and not touchesTopBorder

			if notTouchingLeftAndTop:
				totalSumSubmatrix += sumsMatrix[row - size][col - size]
			
			maxSumSeen = max(maxSumSeen, totalSumSubmatrix)

	return maxSumSeen


def getTotalSumMatrix(matrix):

	sumsMatrix = [[0 for col in row] for row in matrix]
	sumsMatrix[0][0] = matrix[0][0]

	for col in range(1, len(matrix[0])):
		sumsMatrix[0][col] = sumsMatrix[0][col - 1] + matrix[0][col]

	for row in range(1, len(matrix)):
		sumsMatrix[row][0] = sumsMatrix[row - 1][0] + matrix[row][0]

	for row in range(1, len(matrix)):
		for col in range(1, len(matrix[row])):
			sumsMatrix[row][col] = matrix[row][col] + sumsMatrix[row][col - 1] + sumsMatrix[row - 1][col] - sumsMatrix[row - 1][col - 1]

	return sumsMatrix
