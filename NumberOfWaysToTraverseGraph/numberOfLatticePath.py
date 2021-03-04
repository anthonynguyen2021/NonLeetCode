# Time = O(min(width, height))
# Space = O(1)

def numberOfWaysToTraverseGraph(width, height):
    return binomial(width+height-2, width-1)

def binomial(n, m):
	if n-m < m:
		m = n-m
	top = bottom = 1
	for i in range(1, m+1):
		bottom *= i
		top *= (n-i+1)	
	return int(top / bottom)
