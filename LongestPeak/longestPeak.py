# Explanation of solution: We compute at each index i of array, is it potentially a peak point?
# Write a helper method that excludes when i = 0 or i = len(array) - 1. For the remaining cases,
# first check if array[i-1] < array[i] > array[i+1], then set the peak length to 3. Do 2 while loops
# to see the right / left tail continue to be part of the peak or not. 

# Time = O(n) - At most, we'll traverse 6n times when calling computePeak helper method. To see this,
# at index i, we  check array[i-1] < array[i], array[i] > array[i+1]. At index i-1, we check if 
# array[i-1] < array[i]. At index i+1, we check if array[i] < array[i+1]. If index i is part of a peak
# where it extends past index i+1 or before index i-1, we have to check array[i] twice. So O(6n).

# Space = O(1) - We're just storing the largest peak size.

def longestPeak(array):
	largestPeak = 0
	for i in range(len(array)):
		peakLength = computePeak(array, i)
		largestPeak = max(largestPeak, peakLength)
	return largestPeak

def computePeak(array, index):
	if index == 0 or index == len(array)-1:
		return 0
	else:
		if array[index-1] >= array[index] or array[index] <= array[index+1]:
			return 0
		peakLength = 3
		left, right = index-1, index+1
		# As long as right has a right neighbor and we have a strictly increasing condition
		while right+1 < len(array) and array[right] > array[right+1]:
			peakLength += 1
			right += 1
		# As long as left has a left neighbor and we have a strictly increasing condition
		while left-1 >= 0 and array[left-1] < array[left]:
			peakLength += 1
			left -= 1
		return peakLength
		
