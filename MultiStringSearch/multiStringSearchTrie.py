

def multiStringSearch(bigString, smallStrings):
	'''
	Explanation of Solution:
	
	The idea is to dump our words in smallStrings in a trie. We iterate through each character in bigString and search our trie. If we find a word -
	this means we hit an '*', then we change the boolean to True corresponding to that word. See code in how we check our trie.

	Explanation of complexities:
	
	Let w be the number of words in smallStrings and s be the length of the largest word inn smallStrings. Let b be the length of bigStrings.
	We iterate through each character in bigString and do a word search using our trie, so O(sb). We build the trie which is O(sw). For space, we build the trie, which is 
	O(sw). In the main function, we store the array of booleans which is the same length as smallStrings. So this is O(w).

	Time: O(sw + sb)
	Space: O(sw)
	'''
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
