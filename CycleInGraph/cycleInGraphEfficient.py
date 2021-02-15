WHITE, BLACK, GREY = 0, 1, 2

def cycleInGraph(edges):
    visit = [WHITE for node in edges]
	for idx in range(len(edges)):
		if visit[idx] != WHITE:
			continue
		isCycle = depthFirstSearch(edges, visit, idx)
		if isCycle:
			return True
	return False

def depthFirstSearch(edges, visit, node):
	visit[node] = BLACK
	for neighbor in edges[node]:
		if visit[neighbor] == BLACK:
			return True
		elif visit[neighbor] == WHITE:
			isCycle = depthFirstSearch(edges, visit, neighbor)
			if isCycle:
				return True
	visit[node] = GREY
	return False
