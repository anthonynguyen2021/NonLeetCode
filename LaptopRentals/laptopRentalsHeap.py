import heapq

# Time = O(nlog n) | Space = O(n)
def laptopRentals(times):
	if len(times) == 0:
		return 0
	sortedTimes = sorted(times, key = lambda x : x[0])
	buildHeap = [sortedTimes[0][1]]
    	minLaptop = 1
	for idx in range(1, len(sortedTimes)):
		currentRental = sortedTimes[idx]
		currentRentalStart, currentRentalEnd = currentRental
		if currentRentalStart < buildHeap[0]:
			heapq.heappush(buildHeap, currentRentalEnd)
			minLaptop = max(minLaptop, len(buildHeap))
		else:
			heapq.heappop(buildHeap)
			heapq.heappush(buildHeap, currentRentalEnd)
	return minLaptop
