# Time = O(2n choose n)
# Space = O(n) due to the dictionary and the recursive function calls on the call stack

# Idea: By memoization. Solution by recursion. A tree with n+1 node has left subtree of size i and right subtree of size n-i where i is in {0, 1, ..., n} and use multiplication rule.
def numberOfBinaryTreeTopologies(n):
	return helperNumTopology(n)

def helperNumTopology(n, memoize={0:1, 1:1, 2:2}):
	if n in memoize:
		return memoize[n]
	total = 0
	for k in range(0, n):
		total += helperNumTopology(k, memoize) * helperNumTopology(n-k-1, memoize)
	memoize[n] = total
	return total
