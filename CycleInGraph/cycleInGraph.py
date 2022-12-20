# Explanation of solution: Uses backtracking to detect cycle.


# Time = O(v + e) where v = # of vertices, e = # of edges in graph
# Space = O(v)
def cycleInGraph(edges):

	visited = [False for node in edges]  # node visited
	currentStack = [False for node in edges]  # current path traversal, see if nodes have been visited

	for i in range(len(edges)):

		if visited[i]:  # current path visiting has visited node i
			continue

		isCycle = depthFirstSearch(edges, visited, currentStack, i)

		if isCycle:  # if we see a cycle
			return True

	return False  # we do not see a cycle


def depthFirstSearch(edges, visited, currentStack, node):
	'''backtracking to detect cycle. Returns boolean to see if there's a cycle or not'''

	visited[node] = True  # Visit node
	currentStack[node] = True

	for neighbor in edges[node]:

		if currentStack[neighbor]:
			return True
		elif not visited[neighbor]:  # see if we can get a cycle from node neighbor and current path traversed

			isCycle = depthFirstSearch(edges, visited, currentStack, neighbor)
			if isCycle:
				return True

	currentStack[node] = False  # No cycle detected so far, so node is removed from currentStack as part of backtracking

	return False
