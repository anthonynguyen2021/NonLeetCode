# Idea (motivation) of solution: 

# Time = O(m+n) where m is the length of characters and n is the length of document
# Space = O(m+n)
def generateDocument(characters, document):
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
