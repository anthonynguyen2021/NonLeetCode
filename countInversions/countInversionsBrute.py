"""
Explanation of solution: For each pair of indices i, j with i < j
(nested for loop - see below), we check if array[i] > array[j].
If so, increment the count.
"""

# Time = O(n^2) | Space = O(1) where n = len(array)
def countInversions(array):
	numInversion = 0
	for i in range(len(array)):

		for j in range(i+1, len(array)):

			if array[i] > array[j]:
				numInversion += 1

	return numInversion
