

# Time = O(n+m)
# Space = O(n)
def underscorifySubstring(string, substring):
	location = mergeOverlappingSubstring(getIntervalsUnderscore(string, substring))
	return insertUnderscoreAtLocation(string, location)


def getIntervalsUnderscore(string, substring):

	stringIdx = 0
	intervalsUnderscore = []

	while stringIdx < len(string):

		newIdx = string.find(substring, stringIdx)

		if newIdx != -1:
			intervalsUnderscore.append([newIdx, newIdx + len(substring)])
			stringIdx = newIdx + 1
		else:
			break

	return intervalsUnderscore


def mergeOverlappingSubstring(intervalsUnderscore):

	if not intervalsUnderscore:
		return []

	location = [intervalsUnderscore[0]]
	previous = location[0]

	for i in range(1, len(intervalsUnderscore)):

		current = intervalsUnderscore[i]

		if current[0] <= previous[1]:
			previous[1] = current[1]
		else:
			location.append(current)

		previous = location[-1]

	return location


def insertUnderscoreAtLocation(string, location):

	stringIdx = 0
	locationIdx = 0
	i = 0
	stringsToConcatenate = []

	while stringIdx < len(string) and locationIdx < len(location):

		if stringIdx == location[locationIdx][i]:
			stringsToConcatenate.append('_')
			if i == 1:
				locationIdx += 1
			i = 1 if i == 0 else 0

		stringsToConcatenate.append(string[stringIdx])
		stringIdx += 1

	if locationIdx < len(location):
		stringsToConcatenate.append('_')
	elif stringIdx < len(string):
		stringsToConcatenate.append(string[stringIdx:])

	return ''.join(stringsToConcatenate)
