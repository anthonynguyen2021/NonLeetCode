# Time = O(n^2) | Space = O(n)
def laptopRentals(times):
	if len(times) == 0:
		return 0
    times.sort(key = lambda x : x[0])
	largestLaptop = 1
	for idx in range(1, len(times)):
		currentLaptopCount = 1
		for j in range(0, idx):
			if times[idx][0] < times[j][1]:
				currentLaptopCount += 1
		largestLaptop = max(largestLaptop, currentLaptopCount)
    return largestLaptop
