# Time = O(logn) where n = len(array)
# Space = O(logn)

# Idea of solution (recursive): Similar to the iterative approach except at each case where we update
# the pointers, we make a recursive call of the function. 

def shiftedBinarySearch(array, target):
	return helperShiftedBinarySearch(array, target, 0, len(array) - 1)

def helperShiftedBinarySearch(array, target, left, right):

	if left > right:
		return -1

	middle = (left + right) // 2

	if target == array[middle]:
		return middle

	if array[left] < array[middle]:

		if array[left] <= target < array[middle]:
			return helperShiftedBinarySearch(array, target, left, middle - 1)
		else:
			return helperShiftedBinarySearch(array, target, middle + 1, right)
	else:

		if array[middle] < target <= array[right]:
			return helperShiftedBinarySearch(array, target, middle + 1, right)
		else:
			return helperShiftedBinarySearch(array, target, left, middle - 1)
