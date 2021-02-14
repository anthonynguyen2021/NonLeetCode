# Time = O(v + e)
# Space = O(v)

def cycleInGraph(edges):
    	visited = [False for node in edges]
	currentStack = [False for node in edges]
	for i in range(len(edges)):
		if visited[i]:
			continue
		isCycle = depthFirstSearch(edges, visited, currentStack, i)
		if isCycle:
			return True
	return False

def depthFirstSearch(edges, visited, currentStack, node):
	visited[node] = True
	currentStack[node] = True
	for neighbor in edges[node]:
		if currentStack[neighbor]:
			return True
		elif not visited[neighbor]:
			isCycle = depthFirstSearch(edges, visited, currentStack, neighbor)
			if isCycle:
				return True
	currentStack[node] = False
	
	return False
