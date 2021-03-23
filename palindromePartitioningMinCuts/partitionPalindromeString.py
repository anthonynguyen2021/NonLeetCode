# Explanation: This approach is built through DP. To see this, we have to solve this on the size of the string from index 0 to index i 
# where i in {0, 1, ..., len(string)-1} and we name this solution DP as cuts array. For i = 0, we see it's 0. For general i, we have string[0:i+1] 
# is a palindrome in which case we have 0 cuts. If not, we look at substring string[j:i+1] and see if it's a palindrome 
# (we have a table look up for this - memoization). If it is, then we have cuts[i] = min(cuts[i], cuts[j-1]+1). We do this for j in {1, ... , i}.
# For the palindrome look up, we have a 2D matrix to do quick lookup for palindrome from index i to index j (including index j). So the rows indicate
# starting at index i and column j indicates ending at index j. So (i, j) entry will compute if string[i:j+1] is a palindrome or not which is about O(n)
# but less depending on i and j.

# To optimize this method, note that we need to make the palindrome function check O(1). The idea is to build the 2D array in an optimal way. For substring of length 1, 
# we populate the diagonals with True, which means it is a palindrome. Then we build from length 2, ... , len(string). For each of this substring of length i,
# we look at substring string[j:i+j] denoted by [a1, ..., ai] just pictorial. We check if a1 == ai. If not, return False. Otherwise, we look if [a2, ..., ai-1] is a palindrome,
# which we computed previously by smallest length above. 

# Time = O(n^3) | Space = O(n^2) 
# Explanation: For time, we have two for loops which is O(n^2) and palindrome function which is O(n), so O(n^3) to build palindrome matrix.
# For cuts, we have for each index, we have a forloop, so O(n^2). For space, we have O(n^2) from the matrix and O(n) from cuts.

def palindromePartitioningMinCuts(string):
	palindrome = [[False for _ in string] for _ in string]
	for i in range(len(string)):
		for j in range(i, len(string)):
			palindrome[i][j] = isPalindrome(string, i, j)
    	cuts = [float('inf') for char in string]
	cuts[0] = 0
	for idx in range(1, len(string)):
		if palindrome[0][idx]:
			cuts[idx] = 0
		else:
			for i in range(1, idx+1):
				if palindrome[i][idx]:
					cuts[idx] = min(cuts[idx], 1 + cuts[i-1])
	return cuts[-1]

def isPalindrome(string, i, j):
	found = True
	left, right = i, j
	while left < right:
		if string[left] != string[right]:
			found = False
			break
		left += 1
		right -= 1
	return found
