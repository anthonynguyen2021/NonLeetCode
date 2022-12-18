

def laptopRentals(times):
	'''
	Explanation of solution:

	Assume that we sort the starting time. The algorithm loops over the list of ordered pairs, so for i in {0, ... , len(time) - 1}, we check
	the largest number of laptop rented out of time[0], ..., time[i]. To see this, loop through j in {0, ..., i - 1} and check if time[j][1] > time[i][0] (increment count by 1).
	This check will tell us that we need to rent out another laptop.

	Explanation of complexities:

	The time follows from the nested loop. Remark: The sorting is O(nlogn) so this doesn't affect the overall time. The space follows
	from no auxilliary space.

	Time: O(n^2) where n = len(times)
	Space: O(1)

	argument:
		times: list[int]

	return:
		largestLaptop: int
	'''
	if len(times) == 0:
		return 0

	times.sort(key=lambda x: x[0])
	largestLaptop = 1

	for idx in range(1, len(times)):

		currentLaptopCount = 1

		for j in range(0, idx):

			if times[idx][0] < times[j][1]:
				currentLaptopCount += 1

		largestLaptop = max(largestLaptop, currentLaptopCount)

	return largestLaptop
