# Time = O(n) | Space = O(h) where h is the height of the tree
def allKindsOfNodeDepths(root):
	countTable = {}
	depthTable = {}
	buildNumberOfNodes(root, countTable)
	buildSumOfDepths(root, depthTable, countTable)
    return sumOfAllDepthsAtNodes(depthTable)

def sumOfAllDepthsAtNodes(depthTable):
	resultsSumAllDepths = 0
	for key in depthTable:
		resultsSumAllDepths += depthTable[key]
	return resultsSumAllDepths

def buildNumberOfNodes(tree, countTable):
	if not tree:
		return 0
	countTable[tree] = 1
	if tree.left:
		buildNumberOfNodes(tree.left, countTable)
		countTable[tree] += countTable[tree.left]
	if tree.right:
		buildNumberOfNodes(tree.right, countTable)
		countTable[tree] += countTable[tree.right]
	return countTable[tree]

def buildSumOfDepths(tree, depthTable, countTable):
	if not tree:
		return 0
	depthTable[tree] = 0
	if tree.left:
		buildSumOfDepths(tree.left, depthTable, countTable)
		depthTable[tree] += depthTable[tree.left] + countTable[tree.left]
	if tree.right:
		buildSumOfDepths(tree.right, depthTable, countTable)
		depthTable[tree] += depthTable[tree.right] + countTable[tree.right]
	return depthTable[tree]


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
