# Time = O(n)
# Space = O(1)
# Solution Idea: We use bucket sort. We count how many times order[0], order[1],  order[2] occurs in array. Then we mutate the input array to reflect the sorted array.
def threeNumberSort(array, order):
  	bucketCount = dict()
	bucketCount[0] = 0
	bucketCount[1] = 0
	bucketCount[2] = 0
	for val in array:
		if val == order[0]:
			bucketCount[0] += 1
		elif val == order[1]:
			bucketCount[1] += 1
		else:
			bucketCount[2] += 1
	for index in range(len(array)):
		if index < bucketCount[0]:
			array[index] = order[0]
		elif index < bucketCount[1] + bucketCount[0]:
			array[index] = order[1]
		else: 
			array[index] = order[2] 
	return array
