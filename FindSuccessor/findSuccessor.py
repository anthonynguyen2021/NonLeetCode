# This is an input class. Do not edit.
class BinaryTree:
	def __init__(self, value, left=None, right=None, parent=None):
		self.value = value
		self.left = left
		self.right = right
		self.parent = parent

# Note that we don't need the tree input, but it's nice to know that node can be
# found by traversing tree
		
		
# Time = O(h) where h is the height of the binary tree
# Space = O(1) 
def findSuccessor(tree, node):
	if node.right:
		return getLeftMostChild(tree, node.right)
	else:
		return getNextParentInOrder(tree, node)
	
def getLeftMostChild(tree, node):
	current = node 
	while current.left:
		current = current.left
	return current

def getNextParentInOrder(tree, node):
	current = node
	while current.parent and current.parent.left != current:
		current = current.parent 
	return current.parent 
