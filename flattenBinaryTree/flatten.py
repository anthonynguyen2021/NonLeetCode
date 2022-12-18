
# This is the class of the input root. Do not edit it.
class BinaryTree:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

def flatten(tree):

	if not tree:
		return None, None

	if not tree.left:
		left = tree
	else:
		leftSubtreeLeft, leftSubtreeRight = flatten(tree.left)
		connect(leftSubtreeRight, tree)
		left = leftSubtreeLeft

	if not tree.right:
		right = tree
	else:
		rightSubtreeLeft, rightSubtreeRight = flatten(tree.right)
		connect(tree, rightSubtreeLeft)
		right = rightSubtreeRight

	return left, right

def connect(left, right):
	left.right = right
	right.left = left
	return None

# Explanation of Solution: Build a recursive method that given a node tree, it returns the left most node and the right most node.
# The base case is when we have tree = None. The other base case is when tree.left = None / tree.right = None. The flattenning of
# the tree is in order traversal, so given a node tree, tree.left's most right node will double connect tree (visualize the traversal
# order of the in order traversal), and given a node tree, tree.right's most left node will double connect tree.

# Explanation of complexity: Note that the recursive calls won't exceed the height, so space is O(d). The time is O(n) since
# we're recursively calling the methods on all of the nodes. The connnect methods done on each node of the tree is O(1).
# Time = O(n) | Space = O(d) where n is # of nodes in the tree and d is the depth of the tree.
def flattenBinaryTree(root):
	left, right = flatten(root)
	return left
