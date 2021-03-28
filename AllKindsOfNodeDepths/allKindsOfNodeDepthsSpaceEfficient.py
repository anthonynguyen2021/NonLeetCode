# Solution Explanation: We perform a post order traversal of the tree. In this order, given node tree, we build tree.left TreeInfo and tree.right TreeInfo that stores
# number of nodes in the subtree, the current sum of depths at tree.left & tree.right, and the sum of all sum of depths at each of the nodes in the subtree (left / right). Using
# these information, we build up these info for the node tree. The number of nodes at tree is tree.left and tree.right number of nodes plus 1. To build tree's sum of depths,
# we look at tree.left. and tree.right 's sum of depths, we add number of nodes in tree.left and tree.right, respectively. Note that tree.left sum of depths plus number of nodes
# in left subtree is the sub of depths for tree except the computation for the right subtree. We do the sume for the right subtree. 

# Explanation of complexities: Space comes from the call stack. The time complexity follows from visiting each node at each step of the post order traversal and doing constant work.

# Time = O(N) | Space = O(d) where d is the depth of the tree.
def allKindsOfNodeDepths(root):
    	return getTreeInfo(root).totalSumOfDepths
	
def getTreeInfo(tree):
	if not tree:
		return TreeInfo(0, 0, 0)
	
	leftTreeInfo = getTreeInfo(tree.left)
	rightTreeInfo = getTreeInfo(tree.right)
	
	numberOfNodes = leftTreeInfo.numberOfNodes + rightTreeInfo.numberOfNodes + 1
	
	leftSumOfDepths = leftTreeInfo.sumOfDepths + leftTreeInfo.numberOfNodes
	rightSumOfDepths = rightTreeInfo.sumOfDepths + rightTreeInfo.numberOfNodes
	sumOfDepths = leftSumOfDepths + rightSumOfDepths
	
	totalSumOfDepths = leftTreeInfo.totalSumOfDepths + rightTreeInfo.totalSumOfDepths + sumOfDepths
	return TreeInfo(numberOfNodes, sumOfDepths, totalSumOfDepths)
	

class TreeInfo:
	def __init__(self, numberOfNodes, sumOfDepths, totalSumOfDepths):
		self.numberOfNodes = numberOfNodes
		self.sumOfDepths = sumOfDepths
		self.totalSumOfDepths = totalSumOfDepths

# This is the class of the input binary tree.
class BinaryTree:
    	def __init__(self, value):
        	self.value = value
        	self.left = None
        	self.right = None
