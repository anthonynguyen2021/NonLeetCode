

def mergeOverlappingIntervals(intervals):
	'''
	Explanation of solution:
	
	See question prompt for the explanation.

	Complexity explanation:
	
	nlogn time due to sorting. For space, we store at most n items due to disjoint intervals.

	Time: O(nlogn) where n = len(intervals)
	Space: O(n)
	'''
	if not len(intervals):
		return []

	sortedIntervals = sorted(intervals, key=lambda x: x[0])
	mergedIntervals = [sortedIntervals[0][:]]

	for idx in range(1, len(sortedIntervals)):

		currentInterval = sortedIntervals[idx]
		start, end = currentInterval[0], currentInterval[1]

		if start <= mergedIntervals[-1][1]:
			mergedIntervals[-1] = [mergedIntervals[-1][0], max(end, mergedIntervals[-1][1])]
		else:
			mergedIntervals.append(currentInterval)

	return mergedIntervals
