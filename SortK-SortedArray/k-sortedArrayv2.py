import heapq
# Time = O(k + nlogk) | Space = O(k)
def sortKSortedArray(array, k):
  if not array or k == 0:
	  return array
	minHeap = array[:min(k, len(array))]
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
