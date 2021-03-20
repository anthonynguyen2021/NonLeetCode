import heapq
# Time = O(log n) - used to heap push and heap pop at each call of insert.
# Space = O(n) to store max / min heap
class ContinuousMedianHandler:
    def __init__(self):
        self.max_heap = []
	self.min_heap = []
        self.median = None

    def insert(self, number):
        heapq.heappush(self.max_heap, -heapq.heappushpop(self.min_heap, number))
		if len(self.max_heap) > len(self.min_heap):
			heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
		self.median = self.min_heap[0] if len(self.min_heap) != len(self.max_heap) else 0.5 * (self.min_heap[0] + (-self.max_heap[0]))

    def getMedian(self):
        return self.median
