

# Idea of solution: Keep track of how many points each team has as we go through each game and see the results from the result array.
# We would want to keep a counter of the largest number of points seen and store the team name with those points.

# Time O(n) | Space O(k) where k is the number of distinct teams and n = len(results)
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
