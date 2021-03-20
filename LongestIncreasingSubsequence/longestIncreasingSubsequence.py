# Time = O(n^2) | Space = O(n)
def longestIncreasingSubsequence(array):
    longestSubsequence = [1 for _ in array]
	previousIdx = [None for _ in array]
	largestIdx = 0
	for i in range(1, len(array)):
		for j in range(0, i):
			if array[i] > array[j] and longestSubsequence[j] + 1 > longestSubsequence[i]:
				longestSubsequence[i] = longestSubsequence[j] + 1
				previousIdx[i] = j
		if longestSubsequence[i] > longestSubsequence[largestIdx]:
			largestIdx = i
	return buildSubsequence(array, previousIdx, largestIdx)

def buildSubsequence(array, previousIdx, largestIdx):
	currentIdx = largestIdx
	subsequence = []
	while currentIdx != None:
		subsequence.append(array[currentIdx])
		currentIdx = previousIdx[currentIdx]
	return list(reversed(subsequence))
