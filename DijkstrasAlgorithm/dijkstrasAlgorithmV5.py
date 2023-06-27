import heapq

# Time = O(v^2logv + e) | Space = O(v) where v = # of vertices, e = # of edges in the graph
# Explanation of complexities - worst case is we perform v heap operations.
# Also, we visit every edge. Hence time = O(vlogv + e). For space, this is due to result
# and heap.

# Explanation: We use a minheap to store current distance of node (smallest) and
# node. While the heap is not empty, we pop off the heap, look at neighbors, update
# distance of neighbors if smallest. If neighbor is not visited, add neighbors in the list
# of visited and push onto the heap. Return result.


def dijkstrasAlgorithm(start, edges):

	# Intialize data structure for shortest distance
	result = [float('inf')] * len(edges)
	result[start] = 0
	visited = set([])
	minHeap = [(0, start)]

	while len(minHeap) > 0:

		currentDistance, node = heapq.heappop(minHeap)  # currentDistance is the shortest distance from start to node (assuming node hasn't been visited)

		if node in visited:
			continue

		visited.add(node)
		
		for neighborNode, distance in edges[node]:

			if neighborNode in visited: # it's possible that node appeared in minHeap at least twice - this line is to speed up code
				continue

			result[neighborNode] = min(result[neighborNode], currentDistance + distance)
			heapq.heappush(minHeap, (result[neighborNode], neighborNode))

	return list(map(lambda x : -1 if x == float('inf') else x, result))
