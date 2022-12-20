# Idea of solution: Keep track of the number of visited nodes. If you get to the nth node, check to see
# if the index == 0 (assuming you start at index = 0 with no loss in generality); potentially, we may have a cycle where all nodes are visited exactly once. 
# We need to somehow check if nodes in between node 1, ..., node n are all distinct. Next, we need to somehow check the following:

# Graph
# 0 -> 1 -> 2 -> .... -> n  
# Assuming node n is the same as node 0, we need to check that node 1, 2, ... , n corresponds to distinct
# indices in our array. If not, then there are two nodes, say node i & j so that they equal. If either
# one is the same as node n, we need to check for that. Assume node i & j are not the same as node n.
# Note this is impossible since i -> i + 1 -> ... -> j -> i + 1 (cycle) does not reach node n.

# Time = O(n) where n is the length of the array
# Space = O(1)

def hasSingleCycle(array):

	startingIdx = 0
	numberVisited = 0

	while numberVisited < len(array):

		if numberVisited > 0 and startingIdx == 0:
			return False

		startingIdx = (startingIdx + array[startingIdx]) % len(array)
		numberVisited += 1

	return startingIdx == 0
