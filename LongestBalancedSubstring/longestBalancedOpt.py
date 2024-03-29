# Explanation of solution: This is similar to the balanced parenthesis problem using a stack except you initialize the stack with -1 - this works nicely on computing the current size of the balancced parenthesis. 
# If you ever pop this, this means that the previous few
# characters were unbalanced parenthesis, so we add index i to our current substring to check but not including. When we see a left parenthesis, push this in. If we see ")",
# pop this out. If we get to length 0 stack, this means that before index i, we're done checking for max size of balanced string. We push i in and check substring from index i+1 and
# on. If the length of the stack isn't 0, we successful have some matching parenthesis by popping the top of the stack, so let's measure the size of the current matching parenthesis 
# from stack[-1]+1 up to the current index. So the current balanced parenthesis starts at stack[-1] + 1 to index i (including). To see this, whatever is on top of the stack is unnecessful in 
# matching with a right parenthesis, so it's the most recent index we have to check for balanced parenthesis. So the substring looks like this

# _           _            .....  _ 
# stack[-1]  stack[-1]+1          i

# So the substring is string[stack[-1]+1 : i+1]

# Explanation: You look through the string which is O(n) time and the stack yields O(n) space.
# Time = O(n) | Space = O(n)
def longestBalancedSubstring(string):

	maxLength = 0
	stackIdx = [-1]

	for i in range(len(string)):

		if string[i] == "(":
			stackIdx.append(i)
		else:

			stackIdx.pop()

			if len(stackIdx) == 0:
				stackIdx.append(i)
			else:
				beginningIdx = stackIdx[-1]
				lengthValidBracket = i - beginningIdx
				maxLength = max(maxLength, lengthValidBracket)

	return maxLength


# Here's another solution where I've mixed it up using enumerate(string).
def longestBalancedSubstring(string):
	'''
	Time: O(n) where n = len(string)
	Space: O(n)
	'''
	maxLength = 0
	stack = [-1]

	for i, char in enumerate(string):

		if char == "(":
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
