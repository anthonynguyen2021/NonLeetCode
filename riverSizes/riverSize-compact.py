from collections import deque


# Time = O(V + E) where V = # of vertices & E = # of edges where m, n = len(matrix), len(matrix[0]), V = mn, E = 4V
# Space: O(V)
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

			# BFS
			visited[rowIdx][colIdx] = True
			r, c = rowIdx, colIdx
			queue = deque([(r, c)])

			while queue:

				r, c = queue.popleft()
				currentSize += 1

				for r0, c0 in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):

					# Check if neighbor is valid, not visited, and is a water
					if (0 <= r0 < len(matrix) and 0 <= c0 < len(matrix[0])) and not visited[r0][c0] and matrix[r0][c0] == 1:
						visited[r0][c0] = True
						queue.append((r0, c0))

			size.append(currentSize)

	return size 
