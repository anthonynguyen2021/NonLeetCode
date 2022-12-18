from collections import deque  # Used for queue

"""
Idea of solution:

We perform a breadth first search where at each node, we perform the sum of depths rooted
at that node using our recursive method and keep a running tally of the total of all sum  nodes depth. 
We assume our tree is balanced.

"""

# Time = O(NlogN) | Space = O(h) where h is the height of the tree.
def allKindsOfNodeDepths(root):

	totalSumOfNodesDepths = 0
	queue = [root]

	while len(queue) > 0:

		node = queue.popleft()
		totalSumOfNodesDepths += sumOfDepthsTree(node)

		if node.left:
			queue.append(node.left)

		if node.right:
			queue.append(node.right)

	return totalSumOfNodesDepths

def sumOfDepthsTree(tree, depth=0):

	if not tree:
		return 0

	return sumOfDepthsTree(tree.left, depth+1) + sumOfDepthsTree(tree.right, depth+1) + depth


# This is the class of the input binary tree.
class BinaryTree:

	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
