# Time = O(n)
# Space = O(h) where h is the height of the tree

# Idea of Solution: Build this by recursion. The solution maybe in a left / right subtree. If not, the solution
# maybe a path from a leaf node (in left / right subtree) to the root node. Otherwise, there might be a solution
# from two points in the left / right subtree where the path crosses the root node. 

# The isssue is that you deal with the case when nodes maybe negative. This is manifested in the base case of the method
# buildMaxPathSum
def maxPathSum(tree):
	maxPathSumTree, maxHeightTree = buildMaxPathSum(tree)
	return maxPathSumTree

def buildMaxPathSum(tree):
	# Base case: Null node - observe the base case is crucial in getting test cases to work like single node -5
	if not tree:
		return -float('inf'), 0
	# Recursive call on left / right subtree
	maxPathSumLeft, maxHeightSumLeft = buildMaxPathSum(tree.left)
	maxPathSumRight, maxHeightSumRight = buildMaxPathSum(tree.right)
	
	# Build potential maximum max path sum such that the path doesn't traverse the root from left/right to right/left
	# subtree - think a path from the root to some leaf node.
	maxHeightTree = max(maxHeightSumLeft + tree.value, maxHeightSumRight + tree.value, tree.value)
	
	# Build max Path sum dealing with cases of root being negative, left or right subtree having negative maxPathSum
	# MaxPathSum is either in the left subtree, right subtree, a path from the root to some leaf node in the left subtree,
	# a path from the root to some leaf node in the right subtree, or a path that traverses the root node but doesn't
	# start / end there.
	maxPathSumTree = max(maxPathSumLeft, maxPathSumRight)
	maxPathSumTree = max(maxPathSumTree, maxHeightSumLeft + tree.value, maxHeightSumRight + tree.value)
	maxPathSumTree = max(maxPathSumTree, maxHeightSumLeft + maxHeightSumRight + tree.value)
	
	return maxPathSumTree, maxHeightTree
