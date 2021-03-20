# Idea of Solution: We write a recursive algorithm to solve this problem. The first entry of the array is the root. We find the first instance in the remaining array from
# index 1 to len(array) - 1 such that it's as large as the root node: call this index preOrderIdx. Note that this method returns the root node of the constructed BST, so 
# in essence, it would need to construct the left subtree and right subtree. The order we construct the left subtree & right subtree doesn't matter, but this is your recursive calls.
# The base case is when the array is empty.

# This is an input class. Do not edit.
class BST:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

# Time = O(n^2) - The worst case is that we have a BST that's just unbalanced - think all nodes only have left children, no right children. So the for loop at each recursive call
# gives us the sum of the first n integers roughly.

# Space = O(n) - Store the BST nodes.
def reconstructBst(preOrderTraversalValues):
	if len(preOrderTraversalValues) == 0:
		return None
    
	rootValue = preOrderTraversalValues[0]
	preOrderIdx = len(preOrderTraversalValues)
	for idx in range(1, preOrderIdx):
		if rootValue <= preOrderTraversalValues[idx]:
			preOrderIdx = idx
			break
	
	leftSubtree = reconstructBst(preOrderTraversalValues[1:preOrderIdx])
	rightSubtree = reconstructBst(preOrderTraversalValues[preOrderIdx:])
	return BST(rootValue, leftSubtree, rightSubtree)
