# Idea: List characters in the string. Reverse the list. Go through the list use two pointers to keep track of the start and end of the word and reverse that sublist. 

# Time: O(n) where n = len(string)
# Space: O(n)

def reverseWordsInString(string):

	characters = [char for char in string]
	reverseList(characters, 0, len(characters) - 1)
	startIdx = 0

	while startIdx < len(characters):

		endIdx = startIdx

		while endIdx < len(characters) and characters[endIdx] != " ":
			endIdx += 1

		reverseList(characters, startIdx, endIdx - 1)
		startIdx = endIdx + 1

	return "".join(characters)


def reverseList(alist, first, second):

	left, right = first, second

	while left < right:

		swap(alist, left, right)
		left += 1
		right -= 1

	return alist


def swap(alist, i, j):
	alist[i], alist[j] = alist[j], alist[i]
