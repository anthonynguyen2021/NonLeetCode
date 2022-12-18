

def mergeSort(array):
	'''
	Time: O(nlogn) where n = len(array)
	Space = O(1) using linked list
	'''
	if len(array) < 2:
		return array

	# Recursion and assume we sorted left and right halves
	mid = len(array) // 2
	left = mergeSort(array[:mid])
	right = mergeSort(array[mid:])
	
	leftIdx = 0
	rightIdx = 0
	index = 0

	# merge the two halves
	while leftIdx < len(left) and rightIdx < len(right):

		if left[leftIdx] <= right[rightIdx]:
			array[index] = left[leftIdx]
			leftIdx += 1
			index += 1
		else:
			array[index] = right[rightIdx]
			rightIdx += 1
			index += 1

	# if we still need to process left or right half
	if leftIdx == len(left):
		array[index:] = right[rightIdx:]
	else:
		array[index:] = left[leftIdx:]

	return array
