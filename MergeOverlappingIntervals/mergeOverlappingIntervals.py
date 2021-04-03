# Time = O(nlogn) | Space = O(n)
def mergeOverlappingIntervals(intervals):
    if not len(intervals):
		return []
	sortedIntervals = sorted(intervals, key=lambda x : x[0])
	mergedIntervals = [sortedIntervals[0][:]]
	for idx in range(1, len(sortedIntervals)):
		currentInterval = sortedIntervals[idx]
		start, end = currentInterval[0], currentInterval[1]
		if start <= mergedIntervals[-1][1]:
			mergedIntervals[-1] = [mergedIntervals[-1][0], max(end, mergedIntervals[-1][1])]
		else:
			mergedIntervals.append(currentInterval)
    return mergedIntervals
