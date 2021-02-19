# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Time = O(n) where n is the number of nodes in the tree
# Space = O(h) where h is the height of the tree
def validateBst(tree):
    return recursiveBSTcheck(tree, float('-inf'), float('inf'))

def recursiveBSTcheck(tree, lower, upper):
	if not tree:
		return True
	if lower <= tree.value and tree.value < upper:
		return recursiveBSTcheck(tree.left, lower, tree.value) and recursiveBSTcheck(tree.right, tree.value, upper)
	else:
		return False
