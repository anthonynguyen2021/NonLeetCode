# Time = O(n^2) from double loop
# Space = O(n) since we're storing subsequence, index, and buildSubsequence method. 
def maxSumIncreasingSubsequence(array):
    subsequence = array[:]
	index = [None for x in array]
	largest = 0
	for i in range(len(array)):
		currVal = array[i]
		for j in range(0, i):
			oldVal = array[j]
			if oldVal < currVal and currVal + subsequence[j] >= subsequence[i]:
				subsequence[i] = currVal + subsequence[j]
				index[i] = j
		if subsequence[i] >= subsequence[largest]:
			largest = i
	return [subsequence[largest], buildSubsequence(array, index, largest)]

def buildSubsequence(array, index, current):
	subsequence = []
	while current != None:
		subsequence.append(array[current])
		current = index[current]
	return list(reversed(subsequence))
