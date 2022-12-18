

def knapsackProblem(items, capacity):
	'''
	Time: O(len(items) * len(capacity))
	Space: O(len(items) * len(capacity))

	Solve using bottom-up DP where dynamicProgramming[row][col + 1] solves the problem using items[:row+1] and up to capacity col + 1.
	'''
	dynamicProgramming = [[0 for _ in range(0, capacity+1)] for row in items]

	# first row
	for i in range(len(dynamicProgramming[0])):

		if items[0][1] <= i:
			dynamicProgramming[0][i] = items[0][0]

	for row in range(1, len(items)):
		for i in range(1, len(dynamicProgramming[0])):

			if items[row][1] <= i:
				dynamicProgramming[row][i] = max(dynamicProgramming[row - 1][i], items[row][0] + dynamicProgramming[row - 1][i - items[row][1]])
			else:
				dynamicProgramming[row][i] = dynamicProgramming[row - 1][i]

	return getSolution(items, dynamicProgramming)


def getSolution(items, matrix):

	getItemsIdx = []
	row, col = len(matrix) - 1, len(matrix[0]) - 1

	while True:

		while row > 0 and matrix[row][col] == matrix[row-1][col]:
			row -= 1

		# Can't use item in row since it has no value.
		if matrix[row][col] == 0:
			row -= 1
		elif row >= 0: # Append row item in items and update col to account for weights.
			getItemsIdx.append(row)
			col -= items[row][1]
			row -= 1

		if row < 0:
			break

	getItemsIdx = list(reversed(getItemsIdx))
	value = sum([items[index][0] for index in getItemsIdx])

	return [value, getItemsIdx]
