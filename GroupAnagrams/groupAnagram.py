# Time = O(w * n * log(n)) where n is the length of the longest string and w is  the number of strings 
# Spacde = O(w * n)
def groupAnagrams(words):
	anagrams = {}
	for string in words:
		sortedString = ''.join(sorted(string))
		if sortedString in anagrams:
			anagrams[sortedString].append(string)
		else:
			anagrams[sortedString] = [string]
	return list(anagrams.values())
