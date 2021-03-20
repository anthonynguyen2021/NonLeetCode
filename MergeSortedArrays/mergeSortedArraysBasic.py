# Idea of solution: We grab an element from each of the k arrays - this element is the array ID.
# So if we grab from the first array, we put 0 as in the 0th array. We initialize an arraysIdx to
# keep track of where we're at in arrays[0], arrays[1], ..., so on. We perform a do while. Put
# the k IDs of the arrays as long as we don't exceed the index limitation for each arrays[j] for j in
# {0, 1, ..., len(arrays)-1}. If we don't append anything break out. Otherwise, we find the smallest. 
# Then we increment the index in arraysIdx corresponding to the smallest's ID. For instance, if the 
# smallest corresponds to the first array in arrays, we increment arraysIdx[0] by 1. 

# Explanation - k for each step in the do while where we do this for n times - the total elements.
# k is the length of arrays. 
# Time = O(kn) | Space = O(n + k)
def mergeSortedArrays(arrays):
    	arrayKthMerge = []
	arrayIdx = [0 for _ in range(len(arrays))]
	while True:
		smallestItemsToCheck = []
		for i in range(len(arrays)):
			if arrayIdx[i] == len(arrays[i]):
				continue
			smallestItemsToCheck.append(i)
		if len(smallestItemsToCheck) == 0:
			break
		nextItem = getNext(smallestItemsToCheck, arrays, arrayIdx)
		arrayKthMerge.append(arrays[nextItem][arrayIdx[nextItem]])
		arrayIdx[nextItem] += 1
	return arrayKthMerge

def getNext(alist, arrays, arrayIdx):
	smallest = alist[0]
	for i in range(1, len(alist)):
		arrayID = alist[i]
		indexOfArrayID = arrayIdx[arrayID]
		if arrays[arrayID][indexOfArrayID] < arrays[smallest][arrayIdx[smallest]]:
			smallest = arrayID
	return smallest
