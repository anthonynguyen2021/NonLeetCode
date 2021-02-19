# Idea of solution: Suppose we have an auxiliary array to store the solution up to index i - call the full array 
# minJump. This approach uses DP. By induction, suppose you want to solve for minJump[i] and you have the 
# solution minJump[j] for j index 0, ..., i-1. Then we look at each index j in {0, ..., i-1}. If j + array[j] >= i, 
# we set minJump[i] = min(minJump[i], minJump[j]+1).

# Time = O(n^2)
# Space = O(n) 
def minNumberOfJumps(array):
    numJumps = [float('inf') for val in array]
	numJumps[0] = 0
	for i in range(1, len(array)):
		for j in range(0, i):
			if j + array[j] >= i:
				numJumps[i] = min(numJumps[i], numJumps[j]+1)
	return numJumps[-1]
