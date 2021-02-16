# Do not edit the class below except for the
# populateSuffixTrieFrom and contains methods.
# Feel free to add new properties and methods
# to the class.
class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)
		
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
