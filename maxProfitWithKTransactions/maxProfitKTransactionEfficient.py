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
