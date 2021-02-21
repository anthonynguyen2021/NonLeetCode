# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

	# To build a heap, we start from the ground up approach. We sift down from right to left and from
	# bottom to top. Building this takes O(n) where n is the number of nodes. To get this,
	# count the number of sifting done in each depth and for each node in each depth.
	
	# Time = O(n)
	# Space = O(1)
    def buildHeap(self, array):
	if len(array) < 2:
		return array
	lastIdx = (len(array) - 2) // 2
	for i in reversed(range(0, lastIdx+1)):
		self.siftDown(array, i, len(array))
	return array
	# Time = O(log n) - depending on what level you're at in the heap.
	# Space = O(1) using the iterative approach.
    def siftDown(self, array, index, endIdx):
	while True:
		left, right = 2 * index + 1, 2 * index + 2
		smallest = index
		if left < endIdx and array[smallest] > array[left]:
			smallest = left
		if right < endIdx and array[smallest] > array[right]:
			smallest = right
		if smallest != index:
			array[index], array[smallest] = array[smallest], array[index]
			index = smallest
		else:
			break

	# Time = O(log n)
	# Space = O(1)
    def siftUp(self, array, index):
	current = index
	parent = (current - 1) // 2  # Parent node is given by (index - 1) // 2
	while parent >= 0:
		if array[current] < array[parent]:
			array[current], array[parent] = array[parent], array[current]
			current = parent
			parent = (current - 1) // 2
		else:
			break
	# If the min heap is not empty, we can peak at it.
	
	# Time = O(1)
	# Space = O(1)
    def peek(self):
        if self.heap:
		return self.heap[0]

	# Time = O(log n) - Swap the minimum element with the last element in the array. Pop out the elemnt.
	# Sift down starting at index 0.
	# Space = O(1) 
    def remove(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
	pop = self.heap.pop()
	self.siftDown(self.heap, 0, len(self.heap))
	return pop
	
	# Time = O(logn) - uses the sift up which is O(log n) in time
	# Space = O(1)
    def insert(self, value):
        self.heap.append(value)
	self.siftUp(self.heap, len(self.heap)-1)
