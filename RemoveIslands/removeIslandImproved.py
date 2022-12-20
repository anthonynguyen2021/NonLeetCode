# Idea of the solution: Do a DFS on the border of the matrix. When we see a 1, change it to a 2.
# Run through the matrix again from row to row. If we see a 2, change it to a 1. Otherwise, if we see
# a 1, change it to 0.

# Time = O(wh) where w is the width of the matrix and h is the height of the matrix
# Space = O(wh) where the auxillary space comes from the stack in the DFS in the worst case.

def removeIslands(matrix):

	for row in range(len(matrix)):
		for col in range(len(matrix[0])):

			isRow = (row == 0) or (row == len(matrix) - 1)
			isCol = (col == 0) or (col == len(matrix[0]) - 1)
			isBorder = isRow or isCol

			if not isBorder:  # Don't do dfs on interior of matrix
				continue

			if matrix[row][col] != 1:  # if this is a 2, we've visited this already
				continue

			depthFirstSearch(matrix, row, col)  # DFS is done on the border of the matrix with value 1

	for row in range(len(matrix)):
		for col in range(len(matrix[0])):

			if matrix[row][col] == 2:
				matrix[row][col] = 1
			elif matrix[row][col] == 1:
				matrix[row][col] = 0

	return matrix


def depthFirstSearch(matrix, i, j):

	stack = [[i, j]]

	while stack:

		[i, j] = stack.pop()
		matrix[i][j] = 2  # First time visiting a border / see removeIsland function
		neighbors = getNeighbors(matrix, i, j)

		for coordinates in neighbors:

			i, j = coordinates[0], coordinates[1]

			if matrix[i][j] != 1:
				continue

			stack.append([i, j])



def getNeighbors(matrix, i, j):

	neighbors = []

	if i > 0:
		neighbors.append([i - 1, j])
	if i < len(matrix) - 1:
		neighbors.append([i + 1, j])
	if j > 0:
		neighbors.append([i, j - 1])
	if j < len(matrix[0]) - 1:
		neighbors.append([i, j + 1])

	return neighbors
