

def longestPalindromicSubstring(string):
	'''
	Idea of solution:
	
	For each substring string[i:j+1], check if it's a palindrome and the longest seen so far.

	Time: O(n^3) <- O(n^2) for each potential substring and O(n) for palindrome where n = len(string)
	Space: O(n) <- to slice the string at the end
	'''
	if not string:
		return ''

	longest = float('-inf')

	for i in range(len(string)):

		for j in range(i, len(string)):

			if palindrome(string, i, j) and j - i + 1 > longest:

				longest = j - i + 1
				longestIdx = [i, j]

	return string[longestIdx[0]: longestIdx[1]+1]


def palindrome(string, i, j):

	left = i
	right = j

	while left < right:

		if string[left] != string[right]:
			return False

		left += 1
		right -= 1

	return True
