# Idea of solution: A brute force solution is to scan the list from left to right and keep track of the first instance of target and the last instance of target. This solution
# however takes time O(n) with no auxillary space. We ask if we can do better than this. One thing we can strive for is time O(log n). This suggests a binary search like algorithm.
# We just modify it. The idea is to run two instances of the modified binary search where if the midpoint points to the target, then we move the right pointer to the left of the 
# midpoint and keep going if we're looking for the left index. For the other case, we move the left index to the right of the middle index. 


# Time: O(log n) where n = len(array)
# Space: O(1)
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
				right = mid - 1
			else:
				lastIdx = mid
				left = mid + 1
		elif array[mid] > target:
			right = mid - 1
		else:
			left = mid + 1

	return firstIdx if goLeft else lastIdx 
