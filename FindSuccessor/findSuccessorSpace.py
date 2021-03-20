# This is an input class. Do not edit.
class BinaryTree:
	def __init__(self, value, left=None, right=None, parent=None):
		self.value = value
		self.left = left
		self.right = right
		self.parent = parent
	
# Idea: Use extra space to store the in-order traversal of the tree. Go through the list and if we see node, return the next in the list. We append None at the end to avoid
# an edge case and makes our code easier to read. 

# Time / Space Analysis
# Time = O(n)
# Space = O(n)
def findSuccessor(tree, node):
	inOrderTraversal = helperInOrder(tree)
	inOrderTraversal.append(None)
	for idx, vertex in enumerate(inOrderTraversal):
		if vertex == node:
			return inOrderTraversal[idx+1]  # This takes care of the care when idx is at the end of the original list
		
def helperInOrder(tree, inOrder=[]):
	if not tree:
		return inOrder 
	
	helperInOrder(tree.left, inOrder)
	inOrder.append(tree)
	helperInOrder(tree.right, inOrder)
	return inOrder 
