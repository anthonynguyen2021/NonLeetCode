

def longestPalindromicSubstring(string):
	'''
	Solution Idea:

	The idea is that each character is the center of the palindrome or characer i and i - 1. 

	Time: O(n^2) - for each character, we test for palindrome which is O(n), and where n = len(string)
	Space: O(n) - returning the string
	'''
	longestDict = {'size': 0, 'index': None}

	for i in range(len(string)):
		testPalindrome(string, i, longestDict)

	return string[longestDict['index'][0]:longestDict['index'][1]+1]

def testPalindrome(string, i, longestDict):

	if i > 0 and string[i] == string[i-1]:

		count = 2
		left = i - 2
		right = i + 1

		while (left >= 0 and right < len(string)) and string[left] == string[right]:

			count += 2
			left -= 1
			right += 1

		if count > longestDict['size']:
			longestDict['index'] = [left + 1, right - 1]
			longestDict['size'] = count

	count = 1
	left = i - 1
	right = i + 1

	while (left >= 0 and right < len(string)) and string[left] == string[right]:

		count += 2
		left -= 1
		right += 1

	if count > longestDict['size']:

		longestDict['index'] = [left + 1, right - 1]
		longestDict['size'] = count
