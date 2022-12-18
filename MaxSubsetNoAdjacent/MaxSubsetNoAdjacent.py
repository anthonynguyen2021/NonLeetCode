

def maxSubsetSumNoAdjacent(array):
	'''
	Time: O(n) where n = len(array)
	Space: O(n) - we can drop this further by mutating the input array. So just O(n) time.
	'''
	if not array:
		return 0
	elif len(array) == 1:
		return array[0]

	maxArr = array[:]
	maxArr[1] = max(array[0], array[1])

	for idx in range(2, len(array)):
		maxArr[idx] = max(array[idx] + maxArr[idx-2], maxArr[idx-1])

	return maxArr[-1]
