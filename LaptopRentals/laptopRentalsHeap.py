import heapq

# Explanation of solution: We sort by the first coordinate of times. As we loop through the sorted time from left to right for idx in {0, ... , len(times)-1}, if 
# sortedTimes[idx][0] < heap[0] where the heap stores the ending time and the top of the heap stores the next person to return the laptop, we push in 
# sortedTimes[idx][1] into the heap and keep track of the size of the heap; this boolean check means that the next person to rent out the laptop rents it out before the next
# person returns it. If sortedTimes[idx][0] >= heap[0], this means the next person who returns the laptop does so before the next person rents out the laptop. In this case,
# we don't increment the count. We pop out and push in sortedTimes[idx][1] into the heap.

# Explanation of complexities: The space comes from the heap storage. The space comes from sorting times array - O(nlogn) - and n insertion / pop from the heap (each are at most
# log n), so O(nlogn).
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
