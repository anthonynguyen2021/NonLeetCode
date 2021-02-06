# Time = O(nlogn)
# Space = O(1)
def minimumWaitingTime(queries):
    cumulativeSum = 0
	queries.sort()
	for idx in reversed(range(0, len(queries)-1)):
		multiplicity = len(queries)-1-idx
		cumulativeSum += multiplicity * queries[idx]
	return cumulativeSum
