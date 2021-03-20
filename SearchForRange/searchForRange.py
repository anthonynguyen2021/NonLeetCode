# Time = O(log n)
# Space = O(1)
def searchForRange(array, target):
	goLeft = True
	left = helperFindRange(array, target, goLeft)
	right = helperFindRange(array, target, False)
	return [left, right]

def helperFindRange(array, target, goLeft):
	firstIdx, lastIdx = -1, -1
	left, right = 0, len(array) - 1
	while left <= right:
		mid = (left + right) // 2
		if array[mid] == target:
			if goLeft:
				firstIdx = mid
				right = mid-1
			else:
				lastIdx = mid
				left = mid+1
		elif array[mid] > target:
			right = mid-1
		else:
			left = mid+1
	return firstIdx if goLeft else lastIdx 
