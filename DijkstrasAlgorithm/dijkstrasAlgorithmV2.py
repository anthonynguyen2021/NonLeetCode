from collections import deque

def dijkstrasAlgorithm(start, edges):
    result = len(edges) * [float('inf')]
	result[start] = 0
	visited = set([start])
	
	queue = deque([start])
	while len(queue) > 0:
		node = queue.popleft()
		shortestDistance = result[node]
		
		for neighbor in edges[node]:
			neighborNode, distance = neighbor
			result[neighborNode] = min(result[neighborNode], shortestDistance + distance)
			if neighborNode not in visited:
				visited.add(neighborNode)
				queue.append(neighborNode)
	
	return list(map(lambda x : -1 if x == float('inf') else x, result))
