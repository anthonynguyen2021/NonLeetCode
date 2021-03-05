def numberOfWaysToTraverseGraph(width, height):
    numberWays = [[1 for i in range(1, height+1)] for i in range(0, 2)]
	for row in range(2, width+1):
		for col in range(2, height+1):
			numberWays[1][col-1] = numberWays[0][col-1] + numberWays[1][col-2]
			numberWays[0][col-1] = numberWays[1][col-1]
	return numberWays[1][-1]
