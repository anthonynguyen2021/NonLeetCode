# Idea of Solution: Use an auxilliary space to keep track of largest seen to the left / right of index i - use two arrays of size n to keep track of this. 
# If the minimum of the largest seen to the left / right of index i is larger than heights[i], it means there are water trapped at index i with area 
# min(largestSeenLeft[i], largestSeenRight[i]) - heights[i]
# To optimize this approach, you can just use extra 1 array of size n and do some overwriting in this array.

# Time = O(n)
# Space = O(n)
def waterArea(heights):
	largestSeenLeft, largestSeenRight = [0 for _ in heights], [0 for _ in heights]
	currentLargestLeft, currentLargestRight = 0, 0
	for i in range(len(heights)):
		largestSeenLeft[i] = currentLargestLeft
		largestSeenRight[len(heights)-1-i] = currentLargestRight
		if heights[i] > currentLargestLeft:
			currentLargestLeft = heights[i]
		if heights[len(heights)-1-i] > currentLargestRight:
			currentLargestRight = heights[len(heights)-1-i]
	totalWater = 0
	for i in range(len(heights)):
		minWaterHeight = min(largestSeenLeft[i], largestSeenRight[i])
		totalWater += (minWaterHeight - heights[i]) if minWaterHeight > heights[i] else 0
	return totalWater
