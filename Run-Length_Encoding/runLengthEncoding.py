# Explanation of solution: 

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
