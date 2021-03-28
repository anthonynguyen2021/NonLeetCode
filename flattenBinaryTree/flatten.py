# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Time = O(n) | Space = O(d) where n is # of nodes in the tree and d is the depth of the tree.
def flattenBinaryTree(root):
    left, right = flatten(root)
	return left

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
