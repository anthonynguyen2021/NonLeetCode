# This is an input class. Do not edit.
class BST:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right


class TreeInfo:
	def __init__(self, visit, value):
		self.visit = visit
		self.value = value


def findKthLargestValueInBst(tree, k):
	'''
	Idea of Solution:

	Note that if we did a reverse in-order traversal, we get a list of nodal values from largest to smallest. By reverse in-order traversal, we mean
	at a current node, visit the right subtree, visit the current node, and visit the left subtree recursively. We need TreeInfo class to store these global variables that 
	track the number of visited nodes and the current value. The idea is to code the reverse in-order traversal (similar to the in-order traversal) and before we visit a node, 
	check if it's at the kth node. If not, increment the visit by 1 and store the current nodal value in value.  
			
	Time: O(h + k) - worst case to get to the largest value is O(h) where h is the depth of the tree. From there, we have k more nodes to visit.
	Space: O(h) due to the call stack from recursion.
	'''
	treeData = TreeInfo(0, None)
	reverseInOrder(tree, k, treeData)
	return treeData.value


def reverseInOrder(tree, k, treeInfo):

	if not tree:
		return

	reverseInOrder(tree.right, k, treeInfo)
	if treeInfo.visit == k:
		return

	treeInfo.visit += 1
	treeInfo.value = tree.value

	reverseInOrder(tree.left, k, treeInfo)
