# Time = O(nlogn) | Space = O(n)
def laptopRentals(times):
    start = [time[0] for time in times]
	end = [time[1] for time in times]
	
	start.sort()
	end.sort()
	
	numberOfLaptops = 0
	startIdx, endIdx = 0, 0
	while startIdx < len(start):
		startTime = start[startIdx]
		endTime = end[endIdx]
		if endTime <= startTime:
			startIdx += 1
			endIdx += 1
		else:
			numberOfLaptops += 1
			startIdx += 1
    return numberOfLaptops
