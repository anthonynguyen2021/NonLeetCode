

def generateDocument(characters, document):
	'''
	Idea (motivation) of solution:
	
	We want to count how many of character 'a' is in characters (for instance) and how many of 'a' is in document without having to pass through 
	characters and document multiple times. So we ideally like to loop through them once. We do need to store each character as we see them, so a hashmap works well since we can
	access them in O(1) time. As we loop through each char in characters, add 1 to the counter. As we loop through document, if we don't see char in document, we can't
	generate the document. If we see char in hashmap (from document), decrement hashmap[char] by 1. Once we do this, check to see if the value is < 0. If so return False.
	Once we're done with the 2 for loops, return True.

	Time = O(m+n) where m is the length of characters and n is the length of document
	Space = O(m+n)
	'''
	hashMapFrequency = {}

	for char in characters:

		if char in hashMapFrequency:
			hashMapFrequency[char] += 1
		else:
			hashMapFrequency[char] = 1

	for char in document:

		if char not in hashMapFrequency:
			return False

		hashMapFrequency[char] -= 1

		if hashMapFrequency[char] < 0:
			return False

	return True
