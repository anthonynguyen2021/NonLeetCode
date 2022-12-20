# Idea of Solution: We use a two pointer approach and sort both lists to exploit this sortedness. We keep track of the minimum distance observe and if we've seen it, store these
# two numbers. Suppose you're at oneIdx, twoIdx. Calculate the distance arrayOne[oneIdx], arrayTwo[twoIdx] and check if the smallest distance is observed or not and record them.
# If arrayOne[oneIdx] < arrayTwo[twoIdx], move oneIdx by one. Note that if we increase twoIdx by one, the distance is going to increase since both lists are sorted. Therefore, 
# we're solving a smallest problem with oneIdx being incremented by one. Otherwise, if arrayOne[oneIdx] > arrayTwo[twoIdx], increment twoIdx by 1. Similarly, incrementing oneIdx 
# is going to increase the distance by the sortedness. In this case, we've decrease the size of arrayTwo by 1 and we're solving a smaller subproblem. mlogm and nlogn are the 
# sorting complexity of sorting the two lists.


# Time = O(nlogn + mlogm) where n, m are lengths of array1, array2 respectively.
# Space = O(1)
def smallestDifference(arrayOne, arrayTwo):

	arrayOne.sort()
	arrayTwo.sort()
	oneIdx = twoIdx = 0
	smallestDistance = float('inf')

	while oneIdx < len(arrayOne) and twoIdx < len(arrayTwo):

		distance = abs(arrayOne[oneIdx] - arrayTwo[twoIdx])

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
