

class BinaryTree:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None


# Time - O(n) (Time to traverse the tree)
# Space - O(n) (Worst case scenario)
def branchSums(root):

	totalSum = []
	helperBranchSums(root, totalSum, 0)

	return totalSum


def helperBranchSums(root, totalSum, val):

	if not root:
		return 
	elif not root.left and not root.right:
		totalSum.append(val + root.value)
	else:
		helperBranchSums(root.left, totalSum, val + root.value)
		helperBranchSums(root.right, totalSum, val + root.value)
