# T = O(V + E) | S = O(V)
def riverSizes(matrix):
    	size = []
	visited = [[False for _ in row] for row in matrix]
	for rowIdx, row in enumerate(matrix):
		for colIdx, col in enumerate(row):
			currentSize = 0
			if matrix[rowIdx][colIdx] != 1:
				continue
			elif visited[rowIdx][colIdx]:
				continue
			visited[rowIdx][colIdx] = True
			# BFS
			r, c = rowIdx, colIdx
			queue = [(r, c)]
			while queue:
				r, c = queue.pop(0)
				currentSize += 1
				for r0, c0 in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
					# Check if neighbor is valid, not visited, and is a water
					if (0 <= r0 < len(matrix) and 0 <= c0 < len(matrix[0])) and not visited[r0][c0] and matrix[r0][c0] == 1:
						visited[r0][c0] = True
						queue.append((r0, c0))
			size.append(currentSize)
	return size 
