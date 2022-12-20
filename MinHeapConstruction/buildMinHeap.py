

# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:

	def __init__(self, array):
		# Do not edit the line below.
		self.heap = self.buildHeap(array)

	'''
	To build a heap, we start from the ground up approach. We sift down from right to left and from
	bottom to top. Building this takes O(n) where n is the number of nodes. To get this,
	count the number of sifting done in each depth and for each node in each depth.
	'''
	def buildHeap(self, array):
		'''
		Time: O(n) where n = len(array)
		Space: O(1)
		'''
		if len(array) < 2:
			return array

		lastIdx = (len(array) - 2) // 2

		for i in reversed(range(0, lastIdx + 1)):
			self.siftDown(array, i, len(array))

		return array

	def siftDown(self, array, index, endIdx):
		'''
		Time: O(log n) - depending on what level you're at in the heap and n = len(array)
		Space: O(1) using the iterative approach.
		'''
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

	def siftUp(self, array, index):
		'''
		Time: O(log n) where n = len(array)
		Space: O(1)
		'''
		current = index
		parent = (current - 1) // 2  # Parent node is given by (index - 1) // 2

		while parent >= 0:

			if array[current] < array[parent]:
				array[current], array[parent] = array[parent], array[current]
				current = parent
				parent = (current - 1) // 2
			else:
				break

	def peek(self):
		'''
		If the min heap is not empty, we can peak at it.

		Time = O(1)
		Space = O(1)
		'''
		if self.heap:
			return self.heap[0]

	def remove(self):
		'''
		Time: O(log n) <- Swap the minimum element with the last element in the array. Pop out the elemnt. n = len(array)
		Sift down starting at index 0.
		Space = O(1) 
		'''
		self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
		pop = self.heap.pop()
		self.siftDown(self.heap, 0, len(self.heap))

		return pop

	def insert(self, value):
		'''
		Time: O(logn) - uses the sift up which is O(log n) in time where n = len(array)
		Space: O(1)
		'''
		self.heap.append(value)
		self.siftUp(self.heap, len(self.heap) - 1)
