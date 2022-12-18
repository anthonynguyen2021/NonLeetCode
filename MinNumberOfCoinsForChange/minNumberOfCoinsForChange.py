

def minNumberOfCoinsForChange(n, denoms):
	'''
	Time = O(d * n) | Space = O(n) where d = len(denoms)

	Idea of solution:

	Use DP. Build the solution up by having only denoms[0], ..., denoms[j] for 0 <= j < len(denoms).
	'''
	minCoins = [float('inf') for _ in range(n + 1)]
	minCoins[0] = 0

	for denom in denoms:
		for amount in range(0, n + 1):

			if denom <= amount:
				minCoins[amount] = min(minCoins[amount], 1 + minCoins[amount-denom])

	return -1 if minCoins[-1] == float('inf') else minCoins[-1]
