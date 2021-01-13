# Time = O(|items| capacity)
# Space = O(|items| capacity)
def knapsackProblem(items, capacity):
    knapsack = [[False for i in range(0, capacity+1)] for j in range(len(items)+1)]
	for i in range(len(items)):
		for j in range(1, capacity+1):
			if items[i][1] <= j:
				knapsack[i+1][j] = max(items[i][0] + knapsack[i][j-items[i][1]], knapsack[i][j])
			else:
				knapsack[i+1][j] = knapsack[i][j]
	return helperKnapsackProblem(items, capacity, knapsack)

def helperKnapsackProblem(items, capacity, knapsack):
	index = []
	maxVal = 0
	row = len(items)
	col = capacity
	while row > 0:
		if knapsack[row][col] != knapsack[row-1][col]:
			index.append(row-1)
			maxVal += items[row-1][0]
			col -= items[row-1][1]
			row -= 1
		else:
			row -= 1
	return [maxVal, list(reversed(index))]
