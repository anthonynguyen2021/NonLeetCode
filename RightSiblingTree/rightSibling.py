# This is the class of the input root. Do not edit it.
class BinaryTree:
    	def __init__(self, value, left=None, right=None):
        	self.value = value
        	self.left = left
        	self.right = right

# Time = O(n) | Space = O(h) where h is the height of the tree
def rightSiblingTree(root):
    	mutate(root, None, False)
	return root

def mutate(node, parent, isLeft):
	if not node:
		return None
	mutate(node.left, node, True)
	right = node.right
	if not parent:
		node.right = None
	elif isLeft:
		node.right = parent.right
	else:
		if not parent.right:
			node.right = None
		else:
			node.right = parent.right.left
	mutate(right, node, False)
