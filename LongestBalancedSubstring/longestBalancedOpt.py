# Time = O(n) | Space = O(n)
def longestBalancedSubstring(string):
	maxLength = 0
    stack = [-1]
	for i in range(len(string)):
		if string[i] == "(":
			stack.append(i)
		else:
			stack.pop()
			if len(stack) == 0:
				stack.append(i)
			else:
				beginningIdx = stack[-1]
				lengthValidBracket = i - beginningIdx
				maxLength = max(maxLength, lengthValidBracket)
	return maxLength
