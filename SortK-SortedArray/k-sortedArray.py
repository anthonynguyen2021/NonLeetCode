# Idea of solution: Let array = [a1, ..., an] and assume k+1 <= n. Assume that at index i, the elements of array in indices 0, ... , i-1 are in the correct position. 
# Then what goes in indice i can be at index i+k. So we need to put the elements in index i, i+1, ..., i+k in a min heap. Pop out the min element and that goes into 
# the index i position. Then we push the element in index i+k+1. At some point, we can't push the elements of array in the heap anymore, so we're at the end of the array.
# As long as the min heap is not empty, pop out the min element and that goes next.

import heapq

# Time = O(k + nlogk) = O(nlogk) where k is building the heap of size k+1 and we need to push and pop at most n times.
# Space = O(k) - store the k+1 elements in the min heap.
def sortKSortedArray(array, k):
	firstK = array[:min(k+1, len(array))]
	heapq.heapify(firstK)
	idxToInsert = 0
	for idx in range(k+1, len(array)):
		minElement = heapq.heappop(firstK)
		array[idxToInsert] = minElement
		idxToInsert += 1
		heapq.heappush(firstK, array[idx])
	while len(firstK) != 0:
		minElement = heapq.heappop(firstK)
		array[idxToInsert] = minElement
		idxToInsert += 1
    	return array
