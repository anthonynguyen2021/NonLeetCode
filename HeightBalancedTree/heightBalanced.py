class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Time = O(n) where n is the number of nodes
# Space = O(h) where h is the height of the binary tree where we use function call stacks
def heightBalancedBinaryTree(tree):
    balanced, height = buildHeightBalanced(tree)
	return balanced

def buildHeightBalanced(tree):
	if not tree:
		return True, -1
	balancedLeft, heightLeft = buildHeightBalanced(tree.left)
	if not balancedLeft:
		return False, -1
	balancedRight, heightRight = buildHeightBalanced(tree.right)
	if not balancedRight:
		return False, -1
	return abs(heightLeft-heightRight) < 2, max(heightLeft, heightRight)+1
