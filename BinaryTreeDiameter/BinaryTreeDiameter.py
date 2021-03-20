# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Store diameter / height in an object for each node
class TreeInfo:
	def __init__(self, diameter, height):
		self.diameter = diameter
		self.height = height

# Time = O(n)
# Space = O(n)
# We use DFS in-order traversal
def binaryTreeDiameter(tree):
	return helperDiameter(tree).diameter

def helperDiameter(tree):
	# Base Case
	if not tree:
		# By convention, height of empty node is -1. Same with diameter. 
		return TreeInfo(-1, -1)
	
	# By recursion, we can solve the problem for the left and right children
	leftTreeInfo = helperDiameter(tree.left)
	rightTreeInfo = helperDiameter(tree.right)
	# the diameter of  the tree could occur either in the left or right subtree
	maxDiameterSeen = max(leftTreeInfo.diameter, rightTreeInfo.diameter)
	# the diameter occurs where there's a path through the root or in the left/right subtree
	# the +2 includes a path that wraps around the root nodes with 2 edges leaving it.
	diameter = max(maxDiameterSeen, leftTreeInfo.height + rightTreeInfo.height + 2)
	# 1 Extra edge from left/right children to root
	height = 1 + max(leftTreeInfo.height, rightTreeInfo.height)
	
	return TreeInfo(diameter, height)
