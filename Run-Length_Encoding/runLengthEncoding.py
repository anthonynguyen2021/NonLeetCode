# Explanation of solution: The idea is to keep track of the previous character seen and count except at index i as you do a for loop through the length of the string.
# At the current character, if you encounter a different one from previous character, append the encoding to a list and update the previous character. If the previous counter 
# is 9, add that to the list and set the counter to 0.

# Time = O(n)
# Space = O(n) to store output

def runLengthEncoding(string):
	count = 1
	previous = string[0]
	storeCharacters = []
	for i in range(1, len(string)):
		current = string[i]
		if current != previous or count == 9:
			storeCharacters.append(str(count) + previous)
			count = 0
			previous = current
		count += 1
	storeCharacters.append(str(count) + previous)
	return "".join(storeCharacters)
