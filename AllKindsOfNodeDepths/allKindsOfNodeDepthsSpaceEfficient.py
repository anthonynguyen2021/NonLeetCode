def allKindsOfNodeDepths(root):
    	return getTreeInfo(root).totalSumOfDepths
	
def getTreeInfo(tree):
	if not tree:
		return TreeInfo(0, 0, 0)
	
	leftTreeInfo = getTreeInfo(tree.left)
	rightTreeInfo = getTreeInfo(tree.right)
	
	numberOfNodes = leftTreeInfo.numberOfNodes + rightTreeInfo.numberOfNodes + 1
	
	leftSumOfDepths = leftTreeInfo.sumOfDepths + leftTreeInfo.numberOfNodes
	rightSumOfDepths = rightTreeInfo.sumOfDepths + rightTreeInfo.numberOfNodes
	sumOfDepths = leftSumOfDepths + rightSumOfDepths
	
	totalSumOfDepths = leftTreeInfo.totalSumOfDepths + rightTreeInfo.totalSumOfDepths + sumOfDepths
	return TreeInfo(numberOfNodes, sumOfDepths, totalSumOfDepths)
	

class TreeInfo:
	def __init__(self, numberOfNodes, sumOfDepths, totalSumOfDepths):
		self.numberOfNodes = numberOfNodes
		self.sumOfDepths = sumOfDepths
		self.totalSumOfDepths = totalSumOfDepths

# This is the class of the input binary tree.
class BinaryTree:
    	def __init__(self, value):
        	self.value = value
        	self.left = None
        	self.right = None
