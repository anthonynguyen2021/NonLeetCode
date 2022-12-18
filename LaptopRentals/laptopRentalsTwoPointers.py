

def laptopRentals(times):
	'''
	Explanation / Logic of solution:

	It's enough to have separate arrays for start time and end time to solve this problem. Sort these two arrays. We have two pointers startIdx and
	endIdx at start & end arrays, respectively. We do the following as long as startIdx < len(start): if end[endIx] > start[startIdx], we increment laptop count and increment the startIdx by 1; 
	this says that the student that is currently renting the laptop is not done with her rental, so we need to rent out another one. If end[endIdx] <= start[startIdx], the 
	student currently renting out the laptop can give her laptop to the other student wanting to rent out the laptop, so we don't increment anything since the number of laptops don't
	change (draw out some examples); we increment both startIdx & endIdx. Note that startIdx >= endIdx by our logic, so the while loop condition makes sense.

	Explanation of complexities:

	The space follows from storing start & end arrays. The time follows from sorting start and end. The while loop is an O(n) time operation.

	Time: O(nlogn) where n = len(times)
	Space: O(n)
	'''
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
