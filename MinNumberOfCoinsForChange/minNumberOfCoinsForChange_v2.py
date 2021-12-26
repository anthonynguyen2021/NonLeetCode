# Time = O(n * size of denoms) | Space = O(n)

# Solution: Solve this by dp / memoization. Create a method that solves
# the problem with input n. Base case is if m in memo, m < 0.

def minNumberOfCoinsForChange(n, denoms):

	memo = {0 : 0}
	
	def dfs(m):
		
		if m in memo:
			return memo[m]
		elif m < 0:
			return float('inf')
		
		minAmount = float('inf')
		
		for coin in reversed(denoms):
			minAmount = min(minAmount, dfs(m - coin) + 1)
				
		memo[m] = minAmount
		
		return memo[m] 
	
	dfs(n)
	
	return memo[n] if memo[n] < float('inf') else -1
		
