# Idea of Solution: 

# Time = O(nlogn + mlogm) where n, m are lengths of array1, array2 respectively.
# Space = O(1)

def smallestDifference(arrayOne, arrayTwo):
  	arrayOne.sort()
	arrayTwo.sort()
	oneIdx = twoIdx = 0
	smallestDistance = float('inf')
	while oneIdx < len(arrayOne) and twoIdx < len(arrayTwo):
		distance = abs(arrayOne[oneIdx]-arrayTwo[twoIdx])
		if distance < smallestDistance:
			smallestDistance = distance
			smallOne = arrayOne[oneIdx]
			smallTwo = arrayTwo[twoIdx]
		if arrayOne[oneIdx] < arrayTwo[twoIdx]:
			oneIdx += 1
		elif arrayOne[oneIdx] > arrayTwo[twoIdx]:
			twoIdx += 1
		else:
			return [smallOne, smallTwo]
	return [smallOne, smallTwo]
