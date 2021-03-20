# Explanation of solution: We use DP to build our solution. The longestSubsequence array is the solution we build where index i is the largest length of subsequence of array[:i+1]
# where index i is included. For index i, we check index j in {0, ... , i-1} to see if we have largest subsequence from array[:j+1] including index j plus index i exceeds what
# is currently stored at longestSubsequence[i]. We keep track of the index in longestSubsequence that corresponds to the largest sized subsequence in array and use previoudIdx
# array to backtrack and build our subsequence where that array notes the previous part of the subsequence.

# Time = O(n^2) | Space = O(n)
# Explanation: Time comes from the two for loop, and space comes from longestSubsequennce & previousIdx array. Note that buildSequence method is O(n) time and space. 
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
