# Time = O(sw + sb) | Space = O(sw)
def multiStringSearch(bigString, smallStrings):
	trie = Trie()
    for idx in range(len(smallStrings)):
		word = smallStrings[idx]
		trie.add(word, idx)
	smallContainedInBig = [False for word in smallStrings]
	for idx in range(len(bigString)):
		smallStringsContainedInBigStrings(bigString, idx, trie.root, smallContainedInBig)
	return smallContainedInBig

def smallStringsContainedInBigStrings(bigString, idx, trieNode, smallContainedInBig):
	for i in range(idx, len(bigString)):
		char = bigString[i]
		if char not in trieNode:
			return
		trieNode = trieNode[char]
		if "*" in trieNode:
			smallContainedInBig[trieNode["*"]] = True

class Trie:
	def __init__(self):
		self.root = {}
		self.endSymbol = "*"
		
	def add(self, word, idx):
		current = self.root
		for letter in word:
			if letter not in current:
				current[letter] = {}
			current = current[letter]
		current[self.endSymbol] = idx
					
