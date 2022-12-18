

def minimumWaitingTime(queries):
	'''
	Time = O(nlogn) where n = len(queries)
	Space = O(n)

	Idea: At each tasks, add the current wait time to the total wait time.
	'''
	queries.sort()
	currentWaitTime = 0
	totalWaitTime = 0

	for i in range(0, len(queries)):

		if i == 0:
			continue

		currentWaitTime += queries[i-1]
		totalWaitTime += currentWaitTime

	return totalWaitTime
