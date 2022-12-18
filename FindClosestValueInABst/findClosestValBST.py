# Time = O(log n) where n = # of nodes in the tree
# Space = O(1)

# Idea of solution: Let a pointer be the current node in the tree. If the current's value = target, 
# we're done. If not, check if we have a closer distance to the target; in other words, current's value
# is the closest to target currently - store that. If target is larger than current's value, you
# need to check the right tree by setting current = current.right. Otherwise, you check the left-subtree
# and set current = current.left

def findClosestValueInBst(tree, target):

	smallestDistance = float('inf')
	current = tree

	while current:

		# Found the closest value
		if current.value == target:
			return current.value

		if abs(current.value - target) < smallestDistance:
			smallestDistance = abs(current.value - target)
			smallestValue = current.value

		if target > current.value:
			current = current.right
		else:
			current = current.left

	return smallestValue


# This is the class of the input tree. Do not edit.
class BST:

	def __init__(self, value):

		self.value = value
		self.left = None
		self.right = None
