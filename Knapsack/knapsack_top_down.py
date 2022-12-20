

def knapsackProblem(items, capacity):
	'''
	Time: O(len(items) * len(capacity)^2)
	Space: O(len(items) * len(capacity))

	Solve using top-down DP / memoization where we use 
	Example: Items = [[1, 2], [4, 3], [5, 6], [6, 7]], capacity = 10.
	'''
    
	memo = {}

	def	dfs(index, m):
		'''
		0 <= index < len(items)
		m = current size
		'''
		
		if (index, m) in memo:
			return memo[(index, m)]
		elif m < 0:
			return float('-inf')
		elif index < 0:
			return 0
		
		maxAmount = 0
		
		for idx in reversed(range(0, index + 1)):
			maxAmount = max(maxAmount, items[idx][0] + dfs(idx - 1, m - items[idx][1]))
			
		memo[(index, m)] = maxAmount
		
		return memo[(index, m)]
	
	for idx in reversed(range(0, len(items))):

		for idx_j in reversed(range(0, capacity + 1)):
			dfs(idx, idx_j)

	def getSolution(items, memo):

		getItemsIdx = []
		row, col = len(items) - 1, capacity

		while True:

			while row > 0 and memo[(row, col)] == memo[(row - 1, col)]:
				row -= 1

			# Can't use item in row since it has no value.
			if memo[(row, col)] == 0:
				row -= 1
			elif row >= 0:
				getItemsIdx.append(row)
				col -= items[row][1]
				row -= 1

			if row < 0:
				break

		getItemsIdx = list(reversed(getItemsIdx))
		value = sum([items[index][0] for index in getItemsIdx])
		return [value, getItemsIdx]

	return getSolution(items, memo)
