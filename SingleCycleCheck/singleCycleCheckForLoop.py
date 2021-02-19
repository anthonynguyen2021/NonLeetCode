# When length == {0, 1}, this is fine. The solution here implements a for-loop of checking if there's a cycle. Note that the if statement is executed after the jump below.
# We're checking to see if node 1, ..., node n-1 is equal to node n.

# Time = O(n) where n is the length of the array
# Space = O(1)

def hasSingleCycle(array):
    	startingIdx = 0
	for i in range(len(array)):
		startingIdx = (startingIdx + array[startingIdx]) % len(array)
		if i < len(array)-1 and startingIdx == 0:
			return False
	return startingIdx == 0
