# Time = O(n)
# Space = O(1)

# Idea of solution: Observe that any contiguous non-empty subarray that sums to a number less than 0, we can disregard. This is an example of a greedy algorithm. 
# The idea is a sliding window problem. At some point, we have a window that starts at the beginning of the idx where the optimal subarray lies and ends where the end of the 
# optimal subarray. Start the window at index = 0. If that number is negative, get rid of it. Otherwise, consider index = 0 as part of the window. We check index 1. 
# Summing array[0] + array[1], if that's at least 0, we keep this window. Keep moving. At each step of the current window, we want to check if we have a largest sum so far.

# We run a for loop and initialize the currentSum to be 0 since there are no previous numbers added. At each iteration i, add the current value array[i] to currentSum and check
# if the largest sum is achieved. If so, record it. Next, if the current sum is negative, reset it to 0.

def kadanesAlgorithm(array):
    	largestSum = float('-inf')
	currentSum = 0
	for idx in range(len(array)):
		currentSum += array[idx]
		if largestSum < currentSum:
			largestSum = currentSum
		if currentSum < 0:
			currentSum = 0
	return largestSum
