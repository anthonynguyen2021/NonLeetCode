class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Idea of solution: We build a helper recursive method that checks if the tree with root node starting at tree is height balanced (bool valued) and height.
# The base case is an empty node where the height by default is -1 and is balanced. Suppose we're given a binary tree with root node tree. By induction, suppose the left subtree
# is height balanced. If not, return False. Suppose the right subtree is height Balanced as well. If not, return False. We can compute the height of the overall tree by
# computing the largest height of the left & right subtree and add one. To check for balanced, return abs(heightLeft-heightRight) < 2
	
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
