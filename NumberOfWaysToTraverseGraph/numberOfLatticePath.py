

def numberOfWaysToTraverseGraph(width, height):
	'''
	Idea of solution:
	
	Imagine we have a lattice of size height - 1 by width - 1. The number of ways to go from top left to bottom right using only down and right moves is the 
	total moves choose number of down moves. This is a very common problem in combinatorics. The idea is to write a helper method for combinating a binomial coefficient. In this
	helper method, we pick the smaller of the two of m, n - m when computing n choose m. We want to compute (n - 1) .... (n - (m - 1)) / (1 * 2 * ... * m); note that there are m products
	and the binomial coefficient is symmetric, so either m or n - m is smaller. So we can replace m <- n - m if n - m is smaller than m.

	Time = O(min(width, height))
	Space = O(1)
	'''
	return binomial(width + height - 2, width - 1)


def binomial(n, m):

	if n - m < m:
		m = n - m

	top = bottom = 1

	for i in range(1, m + 1):
		bottom *= i
		top *= (n - i + 1)

	return int(top / bottom)
