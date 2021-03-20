# Time = O(n) where n is the number of elements in the matrix
# Space = O(n)

# Idea of solution (recursion): Use the 4 pointer approach (similar to iterative approach). 
# Pay attention to the return statement of this recursive method. At each call of the function,
# the spiral array is being populated by the traversal of the outside layer of the matrix. Remove this layer
# and call this function again on this new matrix. Eventually, the pointers (row / col) will cross,
# and you'll return all the items you traversed in the matrix (spiral). Think about the 1xn, nx1, 1x1
# case as this needs to be handled or else you'll double traverse (see below). Make sure your code runs
# on the 2xn, nx2, 2x2 cases. 
def spiralTraverse(array):
	firstRow, lastRow, firstCol, lastCol = 0, len(array)-1, 0, len(array[0])-1
	spiral = []
	return recursiveTraversal(array, spiral, firstRow, lastRow, firstCol, lastCol)

def recursiveTraversal(array, spiral, firstRow, lastRow, firstCol, lastCol):
	if firstRow > lastRow or firstCol > lastCol:
		return spiral
	for idx in range(firstCol, lastCol+1):
		spiral.append(array[firstRow][idx])
	for idx in range(firstRow+1, lastRow+1):
		spiral.append(array[idx][lastCol])
	for idx in reversed(range(firstCol, lastCol)):
		if firstRow == lastRow:
			break
		spiral.append(array[lastRow][idx])
	for idx in reversed(range(firstRow+1, lastRow)):
		if firstCol == lastCol:
			break
		spiral.append(array[idx][firstCol])
	return recursiveTraversal(array, spiral, firstRow+1, lastRow-1, firstCol+1, lastCol-1)
