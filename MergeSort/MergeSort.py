def mergeSort(array):
	# Time = O(nlogn)
	# Space = O(1) using linked list
    if len(array) < 2:
		return array
	mid = len(array) // 2
	left = mergeSort(array[:mid])
	right = mergeSort(array[mid:])
	
	leftIdx = 0
	rightIdx = 0
	index = 0
	while leftIdx < len(left) and rightIdx < len(right):
		if left[leftIdx] <= right[rightIdx]:
			array[index] = left[leftIdx]
			leftIdx += 1
			index += 1
		else:
			array[index] = right[rightIdx]
			rightIdx += 1
			index += 1
	if leftIdx == len(left):
		array[index:] = right[rightIdx:]
	else:
		array[index:] = left[leftIdx:]
	return array
