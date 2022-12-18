""" 
Explanation: The idea is we traverse the tree in a post order traversal manner. We build a count on the number of nodes in the tree rooted at node via recursion. We build the count at
node by first building the count for node.left if it's not None and add that to the count of node where we initialize count to 1. We do the same by first building the count
for node.right. Then we add this count to node's count. Next, we build a recursive method that traverses the tree in a post order traversal and builds the sum of all node's depth
at the tree rooted at 'tree'. We initialize 'tree' to have depth 0. We build the depthTable for tree.left if it's not None. As part of the formula, we add tree.left's node count
and sum of all depth's of the tree rooted at tree.left to 'tree' with attribute sum of all nodes depth. We do the same for tree.right. Once we build this, we loop through
all the keys of depthTable and sum up depthTable[node] and return that value.
"""

# We visit each node and build the dictionaries for countTable and depthTable, so O(n) space and time. Buildsumofdepth funnction is O(n) in time, same with buildNumberOfNodes, and also
# sumOfAllDepthsAtNodes.
# Time = O(n) | Space = O(n) where n is the height of the tree

def allKindsOfNodeDepths(root):

	countTable, depthTable = {}, {}
	buildNumberOfNodes(root, countTable)
	buildSumOfDepths(root, depthTable, countTable)

	return sumOfAllDepthsAtNodes(depthTable)

def sumOfAllDepthsAtNodes(depthTable):

	resultsSumAllDepths = 0
	for key in depthTable:
		resultsSumAllDepths += depthTable[key]

	return resultsSumAllDepths

def buildNumberOfNodes(tree, countTable):

	if not tree:
		return 0

	countTable[tree] = 1

	if tree.left:
		buildNumberOfNodes(tree.left, countTable)
		countTable[tree] += countTable[tree.left]

	if tree.right:
		buildNumberOfNodes(tree.right, countTable)
		countTable[tree] += countTable[tree.right]

	return countTable[tree]

def buildSumOfDepths(tree, depthTable, countTable):

	if not tree:
		return 0

	depthTable[tree] = 0

	if tree.left:
		buildSumOfDepths(tree.left, depthTable, countTable)
		depthTable[tree] += depthTable[tree.left] + countTable[tree.left]

	if tree.right:
		buildSumOfDepths(tree.right, depthTable, countTable)
		depthTable[tree] += depthTable[tree.right] + countTable[tree.right]

	return depthTable[tree]


# This is the class of the input binary tree.
class BinaryTree:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
