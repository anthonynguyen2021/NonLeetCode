# Idea of Approach is via recursion. Note at grid (i, j), to compute this, we need to figure out the number of ways to get to (i-1, j) and (i, j-1) and add them.

def numberOfWaysToTraverseGraph(width, height):
    	if width == 1 or height == 1:
		return 1
	return numberOfWaysToTraverseGraph(width-1, height) + numberOfWaysToTraverseGraph(width, height-1)
