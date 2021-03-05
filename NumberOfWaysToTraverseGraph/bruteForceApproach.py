# Idea of Approach is via recursion. Note at grid (i, j), to compute this, we need to figure out the number of ways to get to (i-1, j) and (i, j-1) and add them.

# Time = Omega(2^(m+n)) - at each node in the grid, we're making 2 function calls. So this is a lower bound; we can't do better than this exponentially, which is really bad. To
# see this, start at the point (m, n). To get to coordinate (i, j) by going left and up via recursive call, we have 2^(m-i + n-j choose n-j) and we sum over all i, j.
# Space = O(m+n) because from (m, n), we go to (m-1, n) or (m, n-1). We do this until one of the coordinate drop to 1 which is approximately O(m+n)
def numberOfWaysToTraverseGraph(width, height):
    	if width == 1 or height == 1:
		return 1
	return numberOfWaysToTraverseGraph(width-1, height) + numberOfWaysToTraverseGraph(width, height-1)
