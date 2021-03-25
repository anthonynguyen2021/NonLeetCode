# Explanation of solution: This is the brute force approach. We look at all substring string[i:j+1] and check if we have a balanced parenthesis. Of course, if the substring
# is of odd length, there's no way we can match all parenthesis (open and closing ones) due to 1 left over. 

# Note to self: endIdx below indicates that we're looking at substring string[startIdx:endIdx]. Note also that depending on the whether startIdx+2 is odd or not, endIdx may
# reach to len(string)-1 or len(string). Be careful to check for this and look for edge cases when string is length 0, 1, 2, and etc. Note that if we incremented by
# ennIdx in range(x, y, b) where b in {3, 4, ...}, be careful to see if endIdx reaches y-b, ..., y-2, y-1, and etc.

# Explanation: This follows from the 2 for-loops and checking if a substring has a balanced parenthesis is O(n). So O(n^3). For space, balancedParen method is O(n) due to the stack.
# Time O(n^3) | Space = O(n)
def longestBalancedSubstring(string):
    	maxLength = 0
	for startIdx in range(0, len(string)):
		for endIdx in range(startIdx+2, len(string)+1, 2):
			if balancedParen(string, startIdx, endIdx):
				maxLength = max(maxLength, endIdx - startIdx)
	return maxLength

def balancedParen(string, i, j):
	stack = []
	for idx in range(i, j):
		char = string[idx]
		if char == "(":
			stack.append(char)
		elif len(stack) > 0:
			stack.pop()
		else:
			return False
	return len(stack) == 0
