# Idea of solution: To exploit a two pointer approach, we need to sort the array. We look over index i in 0, ...., n-3 (which corresponds to potential triplet where the first is
# array[i]). Set left pointer to i+1, right to len(array)-1. If array[i]+array[left]+array[right] == targetSum, add this triplet in and make sure you both increment left and decrement right by
# +1 and -1 respectively (observe this). If array[i]+array[left]+array[right] < targetSum, this means that we need to increment left. Otherwise, decrement right with right -= 1.

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
