"""
Idea of solution: 
We write a recursive method that sums the depth of a rooted tree. We write another recursive method that in a sense does post-order traversal where
we call the method on root.left, root.right, and call the recursive method that sume the depth of a rooted tree at root. The return is the sum of these 3.
"""


# Explanation of complexities: Space O(h) due to call stack. The space is O(NlogN) where we perform the recursive method sumNodesDepth at a given node which is O(# nodes) in time
# and O(h). We assume the tree is balanced. So when we look at root.left and root.right, they both have roughly N / 2 elementss. So at each level, we do O(N) work with logN levels.
# Time O(NlogN) | Space O(h) where h is the height of the tree
def allKindsOfNodeDepths(root):

	if not root:
		return 0

	return allKindsOfNodeDepths(root.left) + allKindsOfNodeDepths(root.right) + sumNodesDepth(root)


# Time = O(N) | Space = O(h) where h is the height of the tree.
def sumNodesDepth(tree, depth=0):

	if not tree:
		return 0

	return sumNodesDepth(tree.left, depth + 1) + sumNodesDepth(tree.right, depth + 1) + depth 


# This is the class of the input binary tree.
class BinaryTree:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
