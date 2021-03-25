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
