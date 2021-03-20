# Time = O(n^2)
# Space = O(1)

# Brute Force Approach: At each index, we count how much water is occupied at this index.
# For now, assume heights[i] = 0. Note that we look at the largest height to the left of index i
# and largest height to the right of index i. The minimum of the two (water height) determines how 
# much water there is at index i. Now, if we assume that heights[i] > 0, we add only when the water 
# height is more than heights[i].
def waterArea(heights):
	if len(heights) < 3:
		return 0
	totalWater = 0
	for i in range(1, len(heights)-1):
		left, leftLargestSeen = i-1, 0
		right, rightLargestSeen = i+1, 0
		while left >= 0:
			if heights[left] > leftLargestSeen:
				leftLargestSeen = heights[left]
			left -= 1
		while right < len(heights):
			if heights[right] > rightLargestSeen:
				rightLargestSeen = heights[right]
			right += 1
		waterHeight = min(leftLargestSeen, rightLargestSeen)
		if waterHeight > heights[i]:
			totalWater += waterHeight - heights[i]
	return totalWater
