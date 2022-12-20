# Using recursion to solve the problem. 

# Time = O(V + E) where V is the vertex size and E is the size of edge sets. m, n = len(matrix), n = len(matrix[0]), V = mn, E = 4V
# Space = O(V + E) 
def riverSizes(matrix):

	visited = [[False for _ in row] for row in matrix]
	river = []
	currentSize = 0

	for i in range(len(matrix)):
		for j in range(len(matrix[0])):

			currentSize = depthFirstSearch(matrix, visited, i, j, currentSize)
			if currentSize > 0:
				river.append(currentSize)
				currentSize = 0

	return river


def depthFirstSearch(matrix, visited, i, j, currentSize):

	if visited[i][j]:
		return currentSize
	visited[i][j] = True

	if matrix[i][j] == 0:
		return currentSize
	currentSize += 1

	neighbors = getNeighbors(matrix, visited, i, j)
	for i, j in neighbors:
		currentSize = depthFirstSearch(matrix, visited, i, j, currentSize)

	return currentSize


def getNeighbors(matrix, visited, i, j):

	neighbors = []

	if i > 0 and not visited[i-1][j]:
		neighbors.append([i - 1, j])

	if i < len(matrix) - 1 and not visited[i+1][j]:
		neighbors.append([i + 1, j])

	if j > 0 and not visited[i][j-1]:
		neighbors.append([i, j - 1])

	if j < len(matrix[0]) - 1 and not visited[i][j+1]:
		neighbors.append([i, j + 1])

	return neighbors
