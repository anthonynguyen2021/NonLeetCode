# Time = O(nlogn)
# Space = O(1)
def heapSort(array):
	heapify(array)
	for idx in reversed(range(1, len(array))):
		swap(array, 0, idx)
		siftDown(array, 0, idx)  # excluding idx
	return array

# Time = O(log n)
def siftDown(array, idx, endIdx):
	while True:
		left = 2 * idx + 1
		right = 2 * idx + 2
		largest = idx
		if left < endIdx and array[largest] < array[left]:
			largest = left
		if right < endIdx and array[largest] < array[right]:
			largest = right
		if largest != idx:
			swap(array, idx, largest)
			idx = largest
		else:
			break

# Time = O(n)
def heapify(array):
	# Get the index of the parent in the second to last row
	last = (len(array) - 2) // 2
	for idx in reversed(range(0, last+1)):
		siftDown(array, idx, len(array))
	return

# O(1)
def swap(array, i, j):
	array[i], array[j] = array[j], array[i]

