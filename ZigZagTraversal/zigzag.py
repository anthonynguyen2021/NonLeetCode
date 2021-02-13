# Time = O(n) where n is the number of elements in the matrix
# Space = O(n)

# Idea of solution: We use a flag to mark if we're going up or down. Initialize row, col = 0, 0
# Starting with going in the down direction. As long as we're not in the left / bottom wall, add the item,
# and go down and left. Add the item (we're on the left / bottom wall). If we're on the bottom wall,
# go right. Otherwise, go down. Now, we switch  the flag goDown to indicate we go up. As long as we're not in the first row or last column,
# we add the item and go up and right. We're currently at the last column or first row. Add the item.
# If we're in the last column, go down. Otherwise, go right. Switch the flag to go down. We do this
# until the row == len(array) or col == len(array[0]).

def zigzagTraverse(array):
    goDown = True
	row, col = 0, 0
	zigzag = []
	while row < len(array) and col < len(array[0]):
		if goDown:
			while col != 0 and row != len(array)-1:
				zigzag.append(array[row][col])
				row += 1
				col -= 1
			zigzag.append(array[row][col])
			goDown = False
			if row == len(array)-1:
				col += 1
			else:
				row += 1
		else:
			while row != 0 and col != len(array[0])-1:
				zigzag.append(array[row][col])
				row -= 1
				col += 1
			zigzag.append(array[row][col])
			goDown = True
			if col == len(array[0])-1:
				row +=1
			else:
				col += 1
	return zigzag
			
