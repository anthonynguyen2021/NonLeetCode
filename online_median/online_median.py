import heapq

# Time = O(nlogn)
# Space = O(n)
def online_median(array):
    max_heap = []
    min_heap = []
    result = []
    
    for data in array:
        heapq.heappush(max_heap, -heapq.heappushpop(min_heap, data))
        if len(max_heap) > len(min_heap):
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        result.append(min_heap[0] if len(min_heap) != len(max_heap) else 0.5 * (min_heap[0] - max_heap[0]))
    return result
