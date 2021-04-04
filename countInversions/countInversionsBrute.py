# Time = O(n^2) | Space = O(1)
def countInversions(array):
    	numInversion = 0
	for i in range(0, len(array)):
		for j in range(i+1, len(array)):
			if array[i] > array[j]:
				numInversion += 1
    	return numInversion
