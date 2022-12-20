

# Time: O(n^2) where n = len(array)
# Space: O(n) 
def rightSmallerThan(array):

	if not array:
		return []

	rightSmallerThan = [0 for _ in array]

	for i in range(0, len(array) - 1):

		count = 0

		for j in range(i + 1, len(array)):
			if array[i] > array[j]:
				count += 1

		rightSmallerThan[i] = count

	return rightSmallerThan
