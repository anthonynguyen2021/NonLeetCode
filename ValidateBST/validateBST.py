# This is an input class. Do not edit.
class BST:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
	
# Idea of solution: The definition of BST is a binary tree where each node has the BST property. This can be done by recursion. The base case is when the node is empty.
# For general tree node, if that node is a left child, you check if its value is strictly less than its parent's value (upper bound); the lower bound is its nearest ancestor where its a right child which you use that ancestor's parental value.
# If the node is a right child, you check if its value is at least as great as its parent's value (lower bound); for the upper bound, find the nearest ancestor that is a left child (use its parental value). To start off the root,
# set lower bound to be -infinity and upperbound to be infinity.

# Time = O(n) where n is the number of nodes in the tree
# Space = O(h) where h is the height of the tree
def validateBst(tree):
	return recursiveBSTcheck(tree, float('-inf'), float('inf'))


def recursiveBSTcheck(tree, lower, upper):

	if not tree: return True

	if lower <= tree.value and tree.value < upper:
		return recursiveBSTcheck(tree.left, lower, tree.value) and recursiveBSTcheck(tree.right, tree.value, upper)
	else:
		return False
