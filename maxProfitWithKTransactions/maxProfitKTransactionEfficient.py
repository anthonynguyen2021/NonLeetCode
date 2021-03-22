# Explanation of pointers: Note that when row == 1, currentRow & oddRowDP are used interchangable as they point to the same thing and previousRow & evenRowDP points to the same
# thing interchangably. When row == 2, previousRow, oddRow point to the same thing by how Python assigns previousRow = oddRowDP and currentRow, evenRowDP point to the same object.
# Reread this if this solution seems strange.

# Explanation of solution: In the previous solution, note that we only used the previous and current row of the DP build up. So two rows are only needed. 

# Time = O(kn) | Space = O(n) where k and n are # of transactions and n = length of prices, respectively.
def maxProfitWithKTransactions(prices, k):
	if not len(prices):
		return 0
	evenRowDP = [0 for _ in prices]
	oddRowDP = [0 for _ in prices]
	for row in range(1, k+1):
		if row % 2 == 1:
			currentRow = oddRowDP
			previousRow = evenRowDP
		else:
			currentRow = evenRowDP
			previousRow = oddRowDP
		maxSeen = float('-inf')
		for col in range(1, len(prices)):
			maxSeen = max(maxSeen, -prices[col-1] + previousRow[col-1])
			currentRow[col] = max(currentRow[col-1], prices[col] + maxSeen)
	return oddRowDP[-1] if k % 2 == 1 else evenRowDP[-1]
