# Idea of the solution: We use auxilliary space to store a sorted version of each string in words.
# Using this auxilliary array, we sort the array and keep track of the corresponding indices it came from
# the original words array. See the indices.sort line on line 14

# Time = O(w * n * logn + n * w * logw) where n is the length of the largest string and w is the size of words
# Note nlogn comes from sorted each string in words and wlogw comes from sorting indices where the n * w*logw
# means we sort the strings in words and that corresponds to the indices being sorted by a key=lambda function
# Space = O(w * n)
def groupAnagrams(words):
    if not words:
		return []
	sortedWords = ["".join(sorted(word)) for word in words]
	indices = [i for i in range(len(words))]
	indices.sort(key=lambda x: sortedWords[x])
	
	result = []
	currentAnagramGroup = []
	currentAnagram = sortedWords[indices[0]]
	for idx in indices:
		currentWord = words[idx]
		currentSortedWord = sortedWords[idx]
		
		if currentSortedWord == currentAnagram:
			currentAnagramGroup.append(currentWord)
		else:
			result.append(currentAnagramGroup)
			currentAnagramGroup = [currentWord]
			currentAnagram = currentSortedWord
	result.append(currentAnagramGroup)
	return result
