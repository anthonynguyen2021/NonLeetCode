# Time = O(n) where n is the number of nodes in the binary tree
# Space = O(h) where h is the height of the tree due to the recursive call stack

# Idea: Build a helper method that returns the diameter of a tree and the height of a tree via recursion. Base case is -1, -1. The induction is assume you solved it
# for the left child and right child, then build the solution.

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    diameter, height = buildDiameter(tree)
	return diameter

def buildDiameter(tree):
	if not tree:
		return -1, -1
	leftDiameter, leftHeight = buildDiameter(tree.left)
	rightDiameter, rightHeight = buildDiameter(tree.right)
	return max(leftDiameter, rightDiameter, leftHeight + rightHeight + 2), max(leftHeight, rightHeight) + 1
