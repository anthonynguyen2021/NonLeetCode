# Time = O(nlogn) | Space = O(n)
def countInversions(array):
    return countInversionsRecursion(array, 0, len(array))
	
def countInversionsRecursion(array, start, end):
	if end - start < 2:
		return 0
	
	middle = (start + end) // 2
	leftCountInversion = countInversionsRecursion(array, start, middle)
	rightCountInversion = countInversionsRecursion(array, middle, end)
	mergedCountInversion = mergeInversions(array, start, middle, end)
	return leftCountInversion + rightCountInversion + mergedCountInversion

def mergeInversions(array, left, middle, end):
	sortedArray = []
	inversionCount = 0
	
	first = left
	last = middle
	
	while first < middle and last < end:
		if array[first] <= array[last]:
			sortedArray.append(array[first])
			first += 1
		else:
			inversionCount += middle - first
			sortedArray.append(array[last])
			last += 1
	sortedArray += array[first:middle] + array[last:end]
	for idx, num in enumerate(sortedArray):
		array[left + idx] = num
	return inversionCount 
	
	
