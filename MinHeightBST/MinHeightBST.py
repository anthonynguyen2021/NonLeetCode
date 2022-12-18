

def minHeightBst(array):
	'''
	Time: O(n) where n = len(array)
	Space: O(n)
	'''
	return minHeightBstHelper(array, 0, len(array) - 1)

def minHeightBstHelper(array, left, right):

	if left > right:
		return None

	# Get the middle of array
	mid = (left + right) // 2

	# Build Node
	val = array[mid]
	tree = BST(val)

	# build left half and build right half
	tree.left = minHeightBstHelper(array, left, mid - 1)
	tree.right = minHeightBstHelper(array, mid + 1, right)

	return tree


class BST:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
