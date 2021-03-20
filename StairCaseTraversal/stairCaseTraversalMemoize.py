# Time = O(kn) where k = maxSteps
# Space = O(n)

# Idea of solution: At height n, you can step 1x and find the number of ways for height n-1. You can step 2x and find # ways for height n-2..... You can step kx and find # ways
# for height n-k. This approach is like fibonnaci problem, but more general. You use a memoization approach to cache the solution. Note that if height < maxSteps, you solve 
# the problem solution[height-1] + .... + solution[1] + solution[0]. Otherwise, solution[n] = solution[n-1] + ... + solution[n-k]. Note that solution[1] = 1. We define
# solution[0] = 1 because if we're at height n and have k = n, then stepping k=n steps, that's 1 way since solution[n] = solution[n-1] + ... + solution[n- (k-1)] + solution[0].
# You can think stepping k=n steps from height 0 to n is 1 way, so solution[0] = 1. You can also think solution[1] = 1 since solution[1] = solution[0] = 1.

def staircaseTraversal(height, maxSteps):
	return buildStairCaseSolution(height, maxSteps, {0:1, 1:1})

def buildStairCaseSolution(height, maxSteps, memoize):
	if height in memoize:
		return memoize[height]
	solution = 0
	for i in reversed(range(1, min(height, maxSteps) + 1)):
		solution += buildStairCaseSolution(height - i, maxSteps, memoize)
	memoize[height] = solution
	return solution
