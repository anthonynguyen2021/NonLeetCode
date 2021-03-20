# Time = O(n) where n is the number of elements in the matrix
# Space = O(n) where you return the list 

# Idea of solution: Without having to worry about the edge case where the number of rows / cols equal to 1 or 2, we keep running a while loop (set of instructions) as long as 
# firstRow <= lastRow (two row pointers) and firstCol <= lastCol (two column pointers). Within this, you start iterating via a for-loop and appending the items as you traverse the
# outside the matrix. Once you're done, move the 4 pointers accordingly (for instance, firstRow += 1, lastRow -= 1). Now, we need to dig deep and worry about the edge cases.
# This is where we look at 2xn, nx2 to see if our code handles it. Then look at 2x2. Next, look at 1xn, nx1. Here, we may add some columns or rows twice, so you need to write a
# condition that prevents this. Finally, look at 1x1 and see if this is handled.

def spiralTraverse(array):
	spiral = []
	firstRow, firstCol = 0, 0
	lastRow, lastCol = len(array)-1, len(array[0])-1
	while firstRow <= lastRow and firstCol <= lastCol:
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
		firstRow += 1
		lastRow -= 1
		firstCol += 1
		lastCol -= 1
	return spiral
