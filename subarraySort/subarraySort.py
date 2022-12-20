# Idea of solution: Imagine a segment of the left and right portions of the array are sorted.
# _____oxxxxxxxo_____ - the _, x, o represent values in the array and assume the segments of xxxx are 
# unsorted; the _______ portions are sorted. The o represents the first instance where o > x and 
# x > o (2nd appearance). Taking the smallest & largest of the oxxxxxxo segments, we find where the 
# smallest go starting at the left and find the where the largest of this segment starting on the right.


# Time = O(n) where n is the length of the array
# Space = O(1)
def subarraySort(array):

	smallest, largest = float('inf'), float('-inf')

	for idx in range(0, len(array) - 1):
		if array[idx] > array[idx+1]:
			smallest = min(smallest, array[idx+1])
			largest = max(largest, array[idx])

	first, last = 0, len(array) - 1

	while first < len(array) and smallest >= array[first]:
		first += 1

	while last >= 0 and largest <= array[last]:
		last -= 1

	return [first, last] if smallest != float('inf') else [-1, -1]
