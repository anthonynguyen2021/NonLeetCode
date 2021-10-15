# Time = O(V+E) | Space = O(V) where V, E are vertices and edges, respectively. This is the classifical BFS algorithm.

# Idea of solution: Start the BFS at the start node. Pop off the front of the queue and for all the neighboring nodes, update the neighboring node's smallest distance
# the smallest distance of the current's node + distance from current to neighboring node (take the min with neighboring's node smallest distance). If neighboring node 
# has not been visited, push into queue, add to visit set. At the end, map all infinities to -1.

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
