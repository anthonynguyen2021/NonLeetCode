import heapq

# Time: O(k + nlogk) where n = len(array)
# Space: O(k)

# Explanation: Push in k elements into the heap and heapify. Look through the remaining elements in array. If for loop doesn't execute, then we have only k elements. Otherwise,
# push in and get the minimum element since position k (python indexing) can belong to index 0.
def sortKSortedArray(array, k):

	if not array or k == 0:
		return array

	minHeap = array[:min(k, len(array))] # For error checking if k >= len(array)
	heapq.heapify(minHeap)
	insertIdx = 0

	for idx in range(min(k, len(array)), len(array)):
		heapq.heappush(minHeap, array[idx])
		array[insertIdx] = heapq.heappop(minHeap)
		insertIdx += 1

	while len(minHeap) > 0:
		array[insertIdx] = heapq.heappop(minHeap)
		insertIdx += 1

	return array
