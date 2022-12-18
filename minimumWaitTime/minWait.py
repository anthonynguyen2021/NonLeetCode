

def minimumWaitingTime(queries):
	'''
	Since the ith task depends on the sum of the previous i - 1 tasks, it makes sense these i - 1 tasks are the smallest. In other words, the smallest i - 1 elements are in the first
	i - 1 slots. So sort the array in place which is O(nlogn). We can do this without extra space by storing all the previous cumulative tasks time and add it to the current time (see code below).

	Time = O(nlogn) where n = len(queries)
	Space = O(n)
	'''
	cumulativeSum = 0
	queries.sort()

	for idx in reversed(range(0, len(queries) - 1)):

		multiplicity = len(queries) - 1 - idx
		cumulativeSum += multiplicity * queries[idx]

	return cumulativeSum
