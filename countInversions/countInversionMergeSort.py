"""
Explanation of solution:

This follows the merge sort algorithm with some modification. The formula is as following. Start with the array. Break it into left
and right pieces where we take middle = (left + right) // 2. The number of inversions is the number of inversions for left (before sorting the left) 
+ the number of inversions for right (before the sorting) + the number of inversions from the merging process (merging the sorted left and sorted right).  
To understanding the # of inversions in the merging process, if the array[first] > array[last], it means that we have an inversion since the left half has an 
element that's larger than the right half - at this point, left and right are sorted already. So we add that. Note array[idx] > array[last] for 
idx in {first, .... , middle-1}. If array[first] <= array[last], we add that to our sortedArray - array[first] - and increment first (no inversions here). 
The base case in this recursive method is an array of length 1 has no inversions, so it returns 0. Similarly with an array of length 0.

Complexities Explanation:

The space comes from the mergeInversions helper method since it combine a left and right array, so we need at most O(n). For the space
the time comes from there are log n levels where at each level, we're doing O(n) merging. For instance, first division, we have n/2 and n/2 array lengths to merge.
2nd level, we have n/4, n/4, n/4, n/4 arrays to merge and we call mergeInversions twice, but still, we have O(n) work.

"""

# Time = O(nlogn) | Space = O(n) where n = len(array)
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
			inversionCount += (middle - first)
			sortedArray.append(array[last])
			last += 1

	sortedArray += (array[first:middle] + array[last:end])

	for idx, num in enumerate(sortedArray):
		array[left + idx] = num

	return inversionCount 
