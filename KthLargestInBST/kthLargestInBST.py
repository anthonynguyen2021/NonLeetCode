# This is an input class. Do not edit.
class BST:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

# Idea of solution: When we traverse a BST in the in-order traversal way, the resulting visited nodes are sorted. We store the list of visited values and look at 
# the len(array)-k index for the kth largest. 

# Time = O(n) - traverse through the tree is n nodes.
# Space = O(n) - store all the node values in the BST. 
def findKthLargestValueInBst(tree, k):
    	inOrderTraversal = []
	inOrderBST(tree, inOrderTraversal)
	return inOrderTraversal[len(inOrderTraversal)-k]

def inOrderBST(tree, alist):
	if not tree:
		return
	inOrderBST(tree.left, alist)
	alist.append(tree.value)
	inOrderBST(tree.right, alist)
	return 
