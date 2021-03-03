# Idea of Solution: Worst case, we have integers that have negative and positive integers. Imagine we partition the array into negative and positive parts. For the negative
# entries array, imagine that we flip it and absolute value the entries. Now, it's clear that we can figure out what the ith entry of the output array, since we have
# a two pointer approach for the negative array and positive array. For the smaller one in absolute value, we insert the square of that in the next entry of the output array.

# Time = O(n)
# Space = O(n)
def sortedSquaredArray(array):
    	idx = 0
	
	while idx < len(array) and array[idx] < 0:
		idx += 1
	if idx == len(array):
		array = flipArray(array)
	if idx == 0 or idx == len(array):
		return squareArray(array)
	
	left = idx - 1
	right = idx
	currentIdx = 0
	
	squaredArray = [0 for _ in array]
	
	while left >= 0 and right < len(array):
		if abs(array[left]) <= array[right]:
			squaredArray[currentIdx] = array[left] ** 2
			left -= 1
		else:
			squaredArray[currentIdx] = array[right] ** 2
			right += 1
		currentIdx += 1
		
	while left >= 0:
		squaredArray[currentIdx] = array[left] ** 2
		left -= 1
		currentIdx += 1
		
	while right < len(array):
		squaredArray[currentIdx] = array[right] ** 2
		right += 1
		currentIdx += 1
		
	return squaredArray
	
def squareArray(array):
	return [val**2 for val in array]

def flipArray(array):
	left, right = 0, len(array)-1
	while left <= right:
		array[left], array[right] = array[right], array[left]
		left += 1
		right -= 1
	return array
