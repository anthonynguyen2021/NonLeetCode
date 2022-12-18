

def longestSubstringWithoutDuplication(string):
	'''
	Brute force approach
	Solution Idea:
	
	At each index of the string, we keep marching until we seee a duplicate. We keep track of the length of this substring and store how to get this substring somewhere.
	Do this from index 0 to len(string) - 1 while keeping track of the largest substring seen so far. Then we return the largest substring.

	Time: O(n^2) where n = len(string)
	Space: O(n)
	'''
	largest = 0
	substring = dict()

	for index in range(len(string)):

		left, right, sizeSubstring = helperSubstring(string, index)

		if sizeSubstring > largest:

			largest = sizeSubstring
			substring['left'] = left
			substring['right'] = right

	return string[substring['left']:substring['right']]


def helperSubstring(string, index):

	left = index
	right = index
	seen = set()

	for i in range(index, len(string)):

		if string[i] in seen:
			break
		else:
			seen.add(string[i])
			right += 1

	return left, right, right - left
