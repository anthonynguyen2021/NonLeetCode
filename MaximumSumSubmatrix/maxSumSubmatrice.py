# Brute force idea:

# Explanation of solution:

# Explanation of complexities:
# Time = O(w * h) | Space = O(w * h) where w is the width and h is the height
def maximumSumSubmatrix(matrix, size):
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
