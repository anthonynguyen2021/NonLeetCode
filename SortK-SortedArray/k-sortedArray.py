import heapq

# Time = O(k + nlogk)
# Space = O(k)
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
