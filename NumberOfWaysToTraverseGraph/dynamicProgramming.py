# Idea: If we had a matrix of size height by width, we can initialize first row and first column by 1 meaning there's only 1 way to get to those coordinates. 
# We loop from 2nd row to end from 2nd column to last column and do the following. If we want to compute the number of ways to get to (i, j), we use the previous entry
# (i-1, j) which is computed in the previous loop and (i, j-1) which was just computed and update (i, j). 

# Observe that we only use the previous row to construct the current row, so it suggest we use only 1 row. Now, observe that if we interchange width & height, our answer doesn't
# change. To see that, observe transposing the matrix. The grid still have the same number of moves but the number of column and row moves are switched. 

# Time = O(width * height)
# Space = O(min(width, height))

def numberOfWaysToTraverseGraph(width, height):
    	numberWays = [1 for i in range(1, width+1)]
	for row in range(2, height+1):
		for col in range(2, width+1):
			numberWays[col-1] = numberWays[col-1] + numberWays[col-2]
	return numberWays[-1]
