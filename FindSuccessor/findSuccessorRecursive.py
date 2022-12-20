

# This is an input class. Do not edit.
class BinaryTree:
	def __init__(self, value, left=None, right=None, parent=None):
		self.value = value
		self.left = left
		self.right = right
		self.parent = parent

# Idea of solution: Write a recursive method to find successor. If we know that we're going downward, we can write a recursive method starting with the node's right child.
# Otherwise, start a recursive method in finding the parent and the correct next order.


# Time = O(h) where h = height of the tree
# Space = O(h)
def findSuccessor(tree, node):

	goDown = False

	if node.right:
		goDown = True
		return recursiveSuccessor(tree, node.right, goDown)
	else:
		return recursiveSuccessor(tree, node, goDown)


def recursiveSuccessor(tree, node, goDown):

	if goDown:
		if not node.left:
			return node
		else:
			return recursiveSuccessor(tree, node.left, goDown)
	else:
		if not node.parent:
			return None
		elif node.parent.left == node:
			return node.parent
		else:
			return recursiveSuccessor(tree, node.parent, goDown)
