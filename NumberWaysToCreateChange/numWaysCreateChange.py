# T = O(denoms * n) | S = O(n)
# Idea of solution: 
# Use DP. Initialize an array of solution at index 0, 1, .. , n
# We build up the solution using denoms[0], ..., denoms[j] 
# for 0 <= j <= len(denoms)-1
def numberOfWaysToMakeChange(n, denoms):
  makeChange = [0 for _ in range(n+1)]
	makeChange[0] = 1
	for denom in denoms:
		for amount in range(0, n+1):
			if denom <= amount:
				makeChange[amount] += makeChange[amount-denom]
	return makeChange[-1]
