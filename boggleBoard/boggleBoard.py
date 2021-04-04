# Time = O(ws + mn*7^s) | Space = O(ws + mn)
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
		neighbors.append([i-1, j-1])
	if i > 0 and j < len(board[0]) - 1:
		neighbors.append([i-1, j+1])
	if i < len(board) - 1 and j < len(board[0]) - 1:
		neighbors.append([i+1, j+1])
	if i < len(board)-1 and j > 0:
		neighbors.append([i+1, j-1])
	if i > 0:
		neighbors.append([i-1, j])
	if i < len(board)-1:
		neighbors.append([i+1, j])
	if j > 0:
		neighbors.append([i, j-1])
	if j < len(board[0]) - 1:
		neighbors.append([i, j+1])
	return neighbors

class Trie:
	def __init__(self):
		self.root = {}
		self.endSymbol = "*"
		
	def add(self, word):
		current = self.root
		for letter in word:
			if letter not in current:
				current[letter] = {}
			current = current[letter]
		current[self.endSymbol] = word
		
