# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
		
class TreeInfo:
	def __init__(self, visit, value):
		self.visit = visit
		self.value = value

def findKthLargestValueInBst(tree, k):
    treeData = TreeInfo(0, None)
	reverseInOrder(tree, k, treeData)
	return treeData.value

def reverseInOrder(tree, k, treeInfo):
	if not tree:
		return
	
	reverseInOrder(tree.right, k, treeInfo)
	if treeInfo.visit == k:
		return 
	treeInfo.visit += 1
	treeInfo.value = tree.value
	reverseInOrder(tree.left, k, treeInfo)
	
	return 
