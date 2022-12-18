

def knuthMorrisPrattAlgorithm(string, substring):
	'''
	Brute force string search. We have no auxiliary space. We check at
	index i in {0, 1, ... , len(string) - 1} if string[i:i+len(substring)]
	matches substring

	Time: O(mn) where m = len(string), n = len(substring)
	Space: O(1)
	'''
	for i in range(len(string)):

		if substringMatch(string, substring, i):
			return True

	return False


def substringMatch(string, substring, i):
	'''
	If the substring of string from index i to the end is smaller than the length of substring, we can't get a match.
	For i = 0, we have the whole string; for i = 1, we have the string from index 1 to len(string) - 1.
	'''

	if len(string) - i < len(substring):
		return False

	left, right = i, 0

	# Since the if statement is false above, we know substring is not bigger than string[i:]. We do a while loop
	# to check as long as right is a valid index and we have a character match. 
	while right < len(substring) and string[left] == substring[right]:
		left += 1
		right += 1

	# This while loop breaks only when we have a substring match - right == len(substring) or when right < len(substring) 
	# in which case, we don't have a match.
	if right == len(substring):
		return True
	else:
		return False
