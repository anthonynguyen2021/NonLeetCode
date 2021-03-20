# Time - O(n)
# Space - O(n)
def minHeightBst(array):
	return minHeightBstHelper(array, 0, len(array) - 1)

def minHeightBstHelper(array, left, right):
	if left > right:
		return None
	mid = (left + right) // 2
	val = array[mid]
	tree = BST(val)
	tree.left = minHeightBstHelper(array, left, mid-1)
	tree.right = minHeightBstHelper(array, mid+1, right)
	return tree
	
class BST:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
