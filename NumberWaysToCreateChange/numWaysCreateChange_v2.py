

def numberOfWaysToMakeChange(n, denoms):
	'''
	Time: O(n * d^2) where d = len(denoms)
	Space: O(n * d)

	Solution: Use top-down dp solution. Use a helper method dfs(m, index) solves the problem using input m using
	denoms[:index+1].
	'''
	
	# Edge case
	if n == 0:
		return 1
	
	memo = {}
    
	def dfs(m, index):
		'''
		this method solves the original problem with input m
		using denoms[:index+1]
		0 <= j <= index < len(denoms)
		'''
		
		if (m, index) in memo:
			return memo[(m, index)]	
		elif m == 0:
			return 1
		elif m < 0 or index < 0:
			return 0
		
		numWays = 0

		for idx in reversed(range(0, index + 1)):
			numWays += dfs(m - denoms[idx], idx) # note that we use idx, not idx - 1 since we can use the coin again.
			
		memo[(m, index)] = numWays
		
		return memo[(m, index)]
	
	dfs(n, len(denoms) - 1)
	
	return memo[(n, len(denoms) - 1)]
