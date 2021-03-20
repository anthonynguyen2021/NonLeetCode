# Brute Force 
# We solve this by DP. At index i, we look at index j in 0, ...., i-1 and asks ourselves if we can jump to index i from index j. If so, we need to store
# the minimum number of jumps at index i by minimum number of jumps at index j plus 1 or we've stored it already.

# Time = O(n^2)
# Space = O(n)
def minNumberOfJumps(array):
	minJumps = [float('inf') for x in array]
	minJumps[0] = 0
	for i in range(1, len(array)):
		for j in range(0, i):
			if j + array[j] >= i:
				minJumps[i] = min(minJumps[i], minJumps[j]+1)
	return minJumps[-1]
