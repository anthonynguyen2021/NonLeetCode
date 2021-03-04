# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Time = O(n)
# Space = O(n)
def findKthLargestValueInBst(tree, k):
    inOrderTraversal = []
	inOrderBST(tree, inOrderTraversal)
	return inOrderTraversal[len(inOrderTraversal)-k]

def inOrderBST(tree, alist):
	if not tree:
		return
	inOrderBST(tree.left, alist)
	alist.append(tree.value)
	inOrderBST(tree.right, alist)
	return 
