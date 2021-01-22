# The approach is to use DP and at each index idx of largestSubsequence, it solves the largest subsequence sum that contains array[idx]. 
# Initially largestSubsequence[idx] = array[idx]. At each idx, we loop through j in 0, ... , idx - 1 and see if array[j] < array[idx] (strictly increasing) and 
# largestSubsequence[j] + array[idx] >= largestSubsequence[i] (we found a larger subsequence sum). We update the largest subsequence seen at index idx and store index j in 
# another array to denote the previous term in the subsequence is j.

# Time = O(n^2) due to double for loop
# Space = O(n) due to storage from largestSubsequence, subsequenceIdx, and the helper method buildSubsequence.
def maxSumIncreasingSubsequence(array):
	largestSubsequence = array[:]
	subsequenceIdx = [None for _ in array]
	largestIdx = 0
	for i in range(len(array)):
		currVal = array[i]
		for j in range(0, i):
			oldVal = array[j]
			if oldVal < currVal and currVal + largestSubsequence[j] >= largestSubsequence[i]:
				largestSubsequence[i] = currVal + largestSubsequence[j]
				subsequenceIdx[i] = j
		if largestSubsequence[i] >= largestSubsequence[largestIdx]:
			largestIdx = i
	return [largestSubsequence[largestIdx], buildSubsequence(array, subsequenceIdx, largestIdx)]

def buildSubsequence(array, subsequenceIdx, current):
	subsequence = []
	while current != None:
		subsequence.append(array[current])
		current = subsequenceIdx[current]
	return list(reversed(subsequence))
