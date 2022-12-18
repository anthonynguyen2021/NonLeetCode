

def minRewards(scores):
	'''
	Idea of solutions #1-3:
	
	At index i, if scores[i-1] < scores[i], you want rewards[i+1] = rewards[i] + 1 - draw a couple of examples. Suppose at index i, you have 
	scores[i] > scores[i+1]; either rewards[i] = rewards[i+1] + 1 or rewards[i] = rewards[i] since the left side might be larger - draw a picture of ann increasing line from the left
	and compare it from a decreasing line from index i to the right.

	Idea of Solution 1:
	
	Note that a local min has reward 1 to be optimal. Initialize rewards = [1 for _ in scores] Go from index 1 to the end. If scores[i] > scores[i-1], 
	set rewards[i] = rewards[i-1] + 1. If scores[i] < scores[i-1], you set rewards[i-1] = max(rewards[i-1], rewards[i] + 1). Now do this for index i - 1: that is, if scores[i-2] > scores[i-1],
	do the same step again. 

	Time: O(n^2) where n = len(scores)
	Space: O(n)
	'''
	rewards = [1 for _ in scores]

	for i in range(1, len(scores)):

		j = i - 1

		if scores[i] > scores[j]:
			rewards[i] = rewards[j] + 1
		else:
			while j >= 0 and scores[j] > scores[j+1]:
				rewards[j] = max(rewards[j], rewards[j+1] + 1)
				j -= 1

	return sum(rewards)
