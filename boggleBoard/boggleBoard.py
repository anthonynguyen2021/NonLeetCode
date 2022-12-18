"""
# Explanation of Solution: The idea is to use a trie data structure to store our words. We need an array (same size as board) to store
# our path we visited in our dfs search. If we start at index (i, j) in our board, we start the traversal. If we have visited at (i, j) 
# return for that traversral. At coordinates (i, j), if the char = board[i][j] is not in our trie, continue. Otherwise, go deeper
# into our trie and search which is set by trieNode = trieNode[char]. Set (i, j) to be visited. Grab all of (i, j) neighbors (8 of them)
# and perform a dfs on these 8. After that, set (i, j) to be unvisited - see code. Noe that wordsInBoard is there in case of
# duplicate strings found. Note that it takes time to put the strings in as keys, but we can store them as references to indices
# of words, so we can do this in O(1). Also, we can't use a letter twice, so once we visited a character, we can't reuse it.
"""

"""
Explanation of Complexities: For the space, we need to create the trie structure which takes ws. To store our output, it takes
ws. The visited array takes ws where w is the number of words in words and s is the length of the largest word in words. 
Dumping the strings in words as keys is ws space. For
time complexity, we have we have ws to build the trie data structure. For each of the entry of mn size board 'board', we have
8 neighbors to check (everything else constant check). Then each of those have 8 neighbors. So we do this 's' times. So 8^s.
Time = O(ws + mn*8^s) | Space = O(ws + mn)
"""


class Trie:
	# class instance variables
	def __init__(self):
		self.root = {}
		self.endSymbol = "*"
	
	# Add word to Trie
	def add(self, word):

		current = self.root

		for letter in word:

			if letter not in current:
				current[letter] = {}
			current = current[letter]

		current[self.endSymbol] = word


def boggleBoard(board, words):

	trie = Trie()

	for word in words:
		trie.add(word)

	visited = [[False for _ in row] for row in board]
	wordsInBoard = {}

	for i in range(len(board)):

		for j in range(len(board[i])):
			explore(i, j, board, trie.root, visited, wordsInBoard)

	return list(wordsInBoard.keys())


def explore(i, j, board, trieNode, visited, wordsInBoard):

	if visited[i][j]:
		return

	char = board[i][j]
	if char not in trieNode:
		return

	trieNode = trieNode[char]
	visited[i][j] = True

	if "*" in trieNode:
		wordsInBoard[trieNode["*"]] = True

	neighbors = getNeighbors(i, j, board)
	for neighbor in neighbors:
		explore(neighbor[0], neighbor[1], board, trieNode, visited, wordsInBoard)

	visited[i][j] = False
	return


def getNeighbors(i, j, board):

	neighbors = []

	if i > 0 and j > 0:
		neighbors.append([i - 1, j - 1])

	if i > 0 and j < len(board[0]) - 1:
		neighbors.append([i - 1, j + 1])

	if i < len(board) - 1 and j < len(board[0]) - 1:
		neighbors.append([i + 1, j + 1])

	if i < len(board) - 1 and j > 0:
		neighbors.append([i + 1, j - 1])

	if i > 0:
		neighbors.append([i - 1, j])

	if i < len(board) - 1:
		neighbors.append([i + 1, j])

	if j > 0:
		neighbors.append([i, j - 1])

	if j < len(board[0]) - 1:
		neighbors.append([i, j + 1])
	return neighbors
