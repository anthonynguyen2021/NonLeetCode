# Time O(n) | Space O(k)
def tournamentWinner(competitions, results):
    hashmap = {}
	largestSeen = float('-inf')
	winnerID = "None"
	for i in range(len(results)):
		winner = competitions[i][1] if results[i] == 0 else competitions[i][0]
		if winner not in hashmap:
			hashmap[winner] = 1
		else:
			hashmap[winner] += 1
		if hashmap[winner] > largestSeen:
			largestSeen = hashmap[winner]
			winnerID = winner
    return winnerID
