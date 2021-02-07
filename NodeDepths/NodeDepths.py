# Time O(n) where n is the number of nodes in the binary tree
# Space = O(h) where h is the height of the tree
def nodeDepths(root):
    return dfs(root, 0, 0)

def dfs(root, depth, current):
	if not root:
		return current
	current += depth
	current = dfs(root.left, depth+1, current)
	current = dfs(root.right, depth+1, current)
	return current



# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
