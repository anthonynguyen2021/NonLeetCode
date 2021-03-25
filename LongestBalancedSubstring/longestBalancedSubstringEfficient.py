# Time = O(n) | Space = O(1)
def longestBalancedSubstring(string):
    leftParenCount = rightParenCount = 0
	maxCount = 0
	for char in string:
		if char == "(":
			leftParenCount += 1
		else:
			rightParenCount += 1
		if leftParenCount == rightParenCount:
			maxCount = max(maxCount, 2 * rightParenCount)
		elif rightParenCount > leftParenCount:
			leftParenCount = rightParenCount = 0
	
	leftParenCount = rightParenCount = 0
	for idx in reversed(range(len(string))):
		char = string[idx]
		if char == ")":
			rightParenCount += 1
		else:
			leftParenCount += 1
		if leftParenCount == rightParenCount:
			maxCount = max(maxCount, 2 * leftParenCount)
		elif leftParenCount > rightParenCount:
			leftParenCount = rightParenCount = 0
	return maxCount
