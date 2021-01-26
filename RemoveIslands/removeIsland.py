# Idea Solution: Perform DFS on the border of the image black pixels. Then iterate through the interior of the image and if we haven't visited the pixel and is black, change
# it to white. 

# Time = O(wh) # w is the width of the matrix and h is the height of the matrix
# Space = O(wh) # The dfs and visited array are responsible for the space.
def removeIslands(matrix):
	visited = [[False for val in row] for row in matrix]
    for row in range(len(matrix)):
		for col in range(len(matrix[0])):
			isRow = (row == 0) or row == (len(matrix)-1)
			isCol = (col == 0) or col == (len(matrix[0])-1)
			isBorder = isRow or isCol
			if not isBorder:
				continue
			if matrix[row][col] != 1:
				continue
			depthFirstSearch(matrix, visited, row, col)
	for row in range(1, len(matrix)-1):
		for col in range(1, len(matrix[0])-1):
			if visited[row][col]:
				continue
			if matrix[row][col] != 1:
				continue
			else:
				matrix[row][col] = 0
	return matrix

def depthFirstSearch(matrix, visited, i, j):
	stack = []
	stack.append((i, j))
	while stack:
		(i, j) = stack.pop()
		if visited[i][j]:
			continue
		visited[i][j] = True
		if matrix[i][j] == 0:
			continue
		neighbors = getNeighbors(visited, i, j)
		for coordinate in neighbors:
			stack.append(coordinate)
	return 

def getNeighbors(visited, i, j):
	neighbors = []
	if i > 0 and not visited[i-1][j]:
		neighbors.append((i-1, j))
	if i < len(visited) - 1 and not visited[i+1][j]:
		neighbors.append((i+1, j))
	if j > 0 and not visited[i][j-1]:
		neighbors.append((i, j-1))
	if j < len(visited[0]) - 1 and not visited[i][j+1]:
		neighbors.append((i, j+1))
	return neighbors 
		
			
