# Time = O(kn) | Space = O(kn) where k and n are # of transactions and n = length of prices, respectively.
def maxProfitWithKTransactions(prices, k):
	if not len(prices):
		return 0
    buildDP = [[0 for _ in prices] for i in range(k+1)]
	for row in range(1, k+1):
		maxSeen = float('-inf')
		for col in range(1, len(prices)):
			maxSeen = max(maxSeen, -prices[col-1] + buildDP[row-1][col-1])
			buildDP[row][col] = max(buildDP[row][col-1], prices[col] + maxSeen)
	return buildDP[-1][-1]
