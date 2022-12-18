

def invertBinaryTree(tree):
	'''
	Idea of solution:

	You can equivalently think if this problem as asking write a function
	that takes in a binary tree so that for each of the node, the left and right children are swap.

	Time: O(n) where n = # of nodes in the tree
	Space: O(h) where h is the height of the tree
	'''
	if not tree:
		return tree

	tree.left, tree.right = tree.right, tree.left
	invertBinaryTree(tree.left)
	invertBinaryTree(tree.right)

	return tree


# This is the class of the input binary tree.
class BinaryTree:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
