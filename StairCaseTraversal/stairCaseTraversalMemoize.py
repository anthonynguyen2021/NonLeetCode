# Time = O(kn)
# Space = O(n)

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
