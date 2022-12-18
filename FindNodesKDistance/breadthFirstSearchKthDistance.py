from collections import deque  # use queue

# This is an input class. Do not edit.
class BinaryTree:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right


def findNodesDistanceK(tree, target, k):
	'''
	1. Find all parents for each nodes.
	2. Find node that corresponds to target
	3. Perform bfs starting at node containing target.

	Time: O(n) - BFS is O(v+e) = O(e) = O(n). DFS is O(n) where n = # of nodes.
	Space: O(n) - due to queue, parent nodes, and seen set.
	'''
	parentsNode = {}
	depthFirstSearchParent(tree, parentsNode)
	targetNode = getNodeFromValue(tree, target, parentsNode)

	return breadthFirstSearch(targetNode, k, parentsNode)

def breadthFirstSearch(node, k, parentsNode):
	# Use a queue data structure to perform a bfs starting at the node target

	seen = {node.value}
	queue = [(node, 0)]

	while queue:

		node, distance = queue.popleft()

		if distance == k:

			distanceKNodes = [nodeKthDistance.value for nodeKthDistance, _ in queue]
			distanceKNodes.append(node.value)

			return distanceKNodes

		neighbors = [parentsNode[node.value], node.left, node.right]

		for node in neighbors:

			if not node:
				continue

			if node.value in seen:
				continue

			seen.add(node.value)
			queue.append((node, distance + 1))

	return []

def depthFirstSearchParent(node, parentsNode, parent=None):

	if not node:
		return

	parentsNode[node.value] = parent
	depthFirstSearchParent(node.left, parentsNode, node)
	depthFirstSearchParent(node.right, parentsNode, node)
	
def getNodeFromValue(node, target, parentsNode):

	if not parentsNode[target]:
		return node

	parent = parentsNode[target]
	if parent.left and parent.left.value == target:
		return parent.left

	return parent.right
