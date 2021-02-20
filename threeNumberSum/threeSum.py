# Time = O(n^2)
# Space = O(n^2) - worst case / O(n) average case
def threeNumberSum(array, targetSum):
	if len(array) < 3:
		return []
	output = []
 	array.sort()
	for i in range(len(array)-2):
		left = i+1
		right = len(array)-1
		while left < right:
			if array[i] + array[left] + array[right] == targetSum:
				output.append([array[i], array[left], array[right]])
				left += 1
				right -= 1
			elif array[i] + array[left] + array[right] < targetSum:
				left += 1
			else:
				right -= 1
	return output 
