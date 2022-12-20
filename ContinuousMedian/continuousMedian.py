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

class ContinuousMedianHandler:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        self.median = None

    def insert(self, number):

        if len(self.max_heap) == len(self.min_heap):
            # We can't just push into max heap. Here's an example: max_heap = [7], min_heap = [10] and we insert 11 into the max heap. 
            # So we push and pop in the min heap to ensure the pop element is less than or equal to the min heap and push the popped element into the max heap.
            heapq.heappush(self.max_heap, -heapq.heappushpop(self.min_heap, number))
            self.median = -self.max_heap[0]
        else:
            heapq.heappush(self.min_heap, -heapq.heappushpop(self.max_heap, -number))
            self.median = 0.5 * (-self.max_heap[0] + self.min_heap[0])

    def getMedian(self):
        return self.median
