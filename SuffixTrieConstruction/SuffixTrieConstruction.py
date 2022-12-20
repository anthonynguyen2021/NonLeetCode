# Do not edit the class below except for the
# populateSuffixTrieFrom and contains methods.
# Feel free to add new properties and methods
# to the class.


class SuffixTrie:

	def __init__(self, string):
		self.root = {}
		self.endSymbol = "*"
		self.populateSuffixTrieFrom(string)
	# Explanation: We populate self.root, which will be our output. We first look at substring from index i to len(array)-1 
	# for i in {0, 1, ..., len(array)-1} sequentially.  So we populate  these substrings. At index i, we form a for-loop
	# from j in {i, ..., len(array)-1}. We check if char[j] is in our current dictionary. If not, set current[j] = {}. 
	# Otherwise, the dictionary was created earlier. Set current = current[j]. At the end of the inner loop, you
	# set current[self.endSymbol] = True.
	# Remark: All these substring are different lengths.
	
	# Time = O(n^2) where n is the length of the input string
	# Space = O(n^2) where each character in the nested loop counts as storage.
	def populateSuffixTrieFrom(self, string):

		for i in range(len(string)):

			current = self.root

			for j in range(i, len(string)):

				char = string[j]
				if char not in current:
					current[char] = {}
				current = current[char]

			current[self.endSymbol] = True

		return self.root
	# Explanation: Suppose you're at index i of input string. You check if string[i] is in the current dictionary.
	# If not, return False. Else, set current = current[string[i]] - in other words, go deeping into the nested dictionary.
	# At the end of the string, you either have * as a key in your dictionary or not.
	
	# Time = O(m) where m is the length of the input string
	# Space = O(1)
	def contains(self, string):

		dictionary = self.root

		for char in string:

			if char in dictionary:
				dictionary = dictionary[char]
			else:
				return False

		return self.endSymbol in dictionary
