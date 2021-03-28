# Time O(NlogN) | Space O(h) where h is the height of the tree
def allKindsOfNodeDepths(root):
    if not root:
		return 0
	return allKindsOfNodeDepths(root.left) + allKindsOfNodeDepths(root.right) + sumNodesDepth(root)

# Time = O(N) | Space = O(h) where h is the height of the tree.
def sumNodesDepth(tree, depth=0):
	if not tree:
		return 0
	return sumNodesDepth(tree.left, depth+1) + sumNodesDepth(tree.right, depth+1) + depth 


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
