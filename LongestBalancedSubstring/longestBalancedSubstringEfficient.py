# Solution idea: The idea is that as we go from left to right or vice versa, the logic still applies. As we go from left to right,
# we keep counter of the number of opening and closing parenthesis. As we loop through the characters in the string, we increment
# the corresponding opening or closing parenthesis. Then we check if # of opening equals # of closing parenthesis. If so,
# we add maxLength = max of maxLength (currently largest seen and initialized to 0) or 2 * (# of closing parenthesis we've seen). 
# Otherwise, if the number of closing exceeds opening parenthesis, we hit the instance where we can't balance the parenthesis.
# So reset the counters of opening & closing to 0. The example why we check both left to right and right to left is the following:
# ((). Note when we go from left to right, we don't update largest balanced bracket.


# Explaination: This follows from two for loops; first goes from left to right and the second goes from right to left. 
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
