# Time = O(n^3)
# Space = O(1)

# Brute Force Solution: Note that the nested loop automatically gives us O(n^2). Summing is on average O(n/2) for subarray of size n. Therefore, the complexity is O(n^3).


def kadanesAlgorithm(array):
    	largestSum = float('-inf')
	for i in range(len(array)):
		for j in range(i, len(array)):
			currentSum = sum(array[i:j+1])
			largestSum = currentSum if currentSum > largestSum else largestSum
	return largestSum
