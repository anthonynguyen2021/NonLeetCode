# Explanation of solution: The idea is that at a given square, we check if it's not 1x1 or row / col indices are out of bound. We create key  
# r1-r2-c1-c2 which corresponds topRow, bottomRow, leftCol, rightCol. We check if this key is in our hashmap - corresponds to have we computed this square yet? 
# If so, return cache[key]. Why do we do this?
# Note that in our recursive method, we'll redo computations, so we need to cache them. See the recursive call to see. If the key is not in our hashmap, then 
# check if the boundaries are zeros. If so, return True. If not, set cache[key] to if any of the following 5 squares have squares of zero. The 5 squares are the following.
# The four is when we pull the corner diagonally inward by 1 unit. For instance, given pointers TopRow, BottomRow, LeftCol, RightCol, we know look at the square
# TopRow+1, BottomRow, LeftCol+1, RightCol. The 5th square is when we all pull the corners simulatenously inward by 1 unit; so the square is 
# TopRow+1, BottomRow-1, LeftCol+1, RightCol-1. Note that pulling all 4 corners and pulling 1 corner only, we can have repeat computations.

# Remark: Note that in this function we wrote, we get every square ~ O(N^3) of them. Draw a picture to see.

# Time Complexity explanation: Note that we have O(N^2) nodes in our matrix. For each of them - treated as the upper left hand corner of the square - and we look
# at all the possible square sizes with that upper left hand corner index (i, j) which is O(N). For each of such square, it takes O(N) to compute if the boundaries
# are all zeros. So O(N^3) squares. For the space, in the worst case, we store all O(N^3) squares in the hashmap, where the keys are 'r1-r2-c1-c2' for instance where
# r and c are rows and columns, respectively. Note that the function call stack is at most O(N). 

# Time = O(N^4) | Space = O(N^3) where N = len(matrix)
def squareOfZeroes(matrix):

	cache = {}
	n = len(matrix)
	
	topRow = 0
	bottomRow = n - 1
	
	leftCol = 0
	rightCol = n - 1

	return hasSquareOfZeros(matrix, topRow, bottomRow, leftCol, rightCol, cache)


def hasSquareOfZeros(matrix, r1, r2, c1, c2, cache):

	if r1 >= r2 or c1 >= c2:
		return False
	
	key = str(r1) + "-" + str(r2) + "-" + str(c1) + "-" + str(c2)

	if key in cache:
		return cache[key]
	
	cache[key] = (
		isSquareOfZeros(matrix, r1, r2, c1, c2) or
		hasSquareOfZeros(matrix, r1 + 1, r2, c1 + 1, c2, cache) or
		hasSquareOfZeros(matrix, r1 + 1, r2, c1, c2 - 1, cache) or
		hasSquareOfZeros(matrix, r1, r2 - 1, c1 + 1, c2, cache) or
		hasSquareOfZeros(matrix, r1, r2 - 1, c1, c2 - 1, cache) or
		hasSquareOfZeros(matrix, r1 + 1, r2 - 1, c1 + 1, c2 - 1, cache)
	
	)
	
	return cache[key]


def isSquareOfZeros(matrix, r1, r2, c1, c2):

	for row in range(r1, r2 + 1):
		if matrix[row][c1] != 0 or matrix[row][c2] != 0:
			return False

	for col in range(c1, c2 + 1):
		if matrix[r1][col] != 0 or matrix[r2][col] != 0:
			return False

	return True
