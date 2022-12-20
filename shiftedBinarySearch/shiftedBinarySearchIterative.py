# Time = O(log n) where n = len(array)
# Space = O(1)

# Idea of Solution (Iterative): We perform a modified binary search algorithm. We use a two pointer
# approach to solve this. If the middle value is not the target, we have two cases. Either 
# the left half is sorted or the right half is sorted. If the left half is sorted, check to see
# if target is in the interval [array[left], array[middle]). If so, set right = middle - 1. If not,
# we check the right half and set left = middle + 1. The other case is when the right half is sorted.
# We check if target is in (array[middle], array[right]]. If so, set left = middle + 1. If not, check the
# left half and set right = middle - 1.

# Remark: Distinct integers is not necessary in which case we can adjust the code slightly below.
def shiftedBinarySearch(array, target):

	left, right = 0, len(array) - 1

	while left <= right:

		middle = (left + right) // 2

		if array[middle] ==  target:
			return middle

		if array[left] < array[middle]:
			if array[left] <= target < array[middle]:
				right = middle - 1
			else:
				left = middle + 1
		else:
			if array[middle] < target <= array[right]:
				left = middle + 1
			else:
				right = middle - 1

	return -1
