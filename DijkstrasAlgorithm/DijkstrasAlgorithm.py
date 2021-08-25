# Idea: The complexity is v^2 * e for time due to looking through the vertices for smallest distance 
# graph traversal is O(v+e). Initialize an array of minimum distance where all is infinity. Set the 
# start index to be 0 distance. we need a visited set. As long as the visited doesn't contain all
# the vertices, get the smallest distance (if smallest is infinity - return), look at all unvisited
# neighbors and if the distance from smallest vertex to its neighbor is smaller than previously recorded
# update it. At the end, map all infinities to -1.

# Time = O(v^2 * e + e) | Space = O(v)
def dijkstrasAlgorithm(start, edges):
    visited = set()
	minimumDistances = [float('inf') for edge in edges]
	minimumDistances[start] = 0
	numVertices = len(minimumDistances)
	
	while len(visited) != numVertices:
		vertex, smallestDistance = getSmallestDistance(minimumDistances, visited)
		if smallestDistance == float('inf'):
			break
		for edge in edges[vertex]:
			currentVertex, currentDistance = edge
			if currentVertex in visited:
				continue
			if smallestDistance + currentDistance < minimumDistances[currentVertex]:
				minimumDistances[currentVertex] = smallestDistance + currentDistance
		visited.add(vertex)
		
	return list(map(lambda x : -1 if x == float('inf') else x, minimumDistances))

def getSmallestDistance(minimumDistances, visited):
	vertex = -1
	smallestDistance = float('inf')
	for idx, distance in enumerate(minimumDistances):
		if idx in visited:
			continue
		if distance < smallestDistance:
			smallestDistance = distance
			vertex = idx
	return vertex, smallestDistance
