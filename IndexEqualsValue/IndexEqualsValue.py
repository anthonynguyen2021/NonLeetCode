

def indexEqualsValue(array):
	'''
	Idea of solution:

	Note that if array[mid] = mid, we need to check the left of mid to see if we get a fixed point. If array[mid] > mid,
	by sortedness of the array, we don't check array[j] where j > mid. So right = mid - 1. Otherwise, set left = mid + 1
	by similar argument.

	Time: O(log n) where n = len(array)
	Space: O(1)
	'''
	index = -1
	left = 0
	right = len(array) - 1

	while left <= right:

		mid = (left + right) // 2

		if array[mid] == mid:
			index = mid
			right = mid - 1
		elif array[mid] > mid:
			right = mid - 1
		else:
			left = mid + 1

	return index 
