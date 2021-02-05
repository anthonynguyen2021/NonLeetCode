# Idea of solution: Go through the string character  by character is keep track of when we first see a white space " ". Then append string[startIdx:i] where 
# i is the ith iteration of the for loop and startIdx is the beginning of the word in the string. However, if string[i] is not " " and string[startIdx] = " ", add " " to the list.
# Note this happens when we have a string that looks like this '..." "x'.

# Time = O(n) where n is the length of the string
# Space = O(n) 
def reverseWordsInString(string):
    startIdx = 0
	words = []
	for idx in range(len(string)):
		char = string[idx]
		# The if elif statement doesn't execute means that we have a character in a word.
		if char == " ":
			words.append(string[startIdx:idx])
			startIdx = idx
		elif string[startIdx] == " ":
			words.append(string[startIdx:idx])
			startIdx = idx
	words.append(string[startIdx:])
	words = reverse(words)
	return "".join(words)

def reverse(alist):
	left = 0
	right = len(alist) - 1
	while left < right:
		alist[left], alist[right] = alist[right], alist[left]
		left += 1
		right -=1
	return alist
		
