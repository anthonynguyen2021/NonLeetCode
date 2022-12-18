

def firstNonRepeatingCharacter(string):
	'''
	Explanation:

	Go through the characters in the string from left to right, if we see the character
	for the first time, hash the character as the key and the count should be set as 1 along with its
	index it appears in the string - use enumerate to get these two. Next, we iterate through
	the key in the dictionary (they'll be listed in the same order as we input them), if we find
	a key whose count is 1, return its index.

	Explanation of complexities:

	Time follows from iterating through the string. The space comes from the
	fact that the alphabet has 26 characters

	Time = O(n) | Space = O(1)

	argument:
		string: str

	return:
		found: str
	'''
	alphabetHashMap = {}
	found = -1

	for idx, char in enumerate(string):

		if char not in alphabetHashMap:
			alphabetHashMap[char] = [1, idx]
		else:
			alphabetHashMap[char][0] += 1

	for key in alphabetHashMap:

		if alphabetHashMap[key][0] == 1:
			found = alphabetHashMap[key][1]
			break

	return found
