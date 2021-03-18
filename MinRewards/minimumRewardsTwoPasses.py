# Time = O(n) | Space = O(n)
def minRewards(scores):
	if len(scores) == 1:
		return 1
	elif len(scores) == 2:
		return 3
    rewards = [1 for _ in scores]
	for i in range(1, len(scores)):
		if scores[i] > scores[i-1]:
			rewards[i] = rewards[i-1] + 1
	for i in reversed(range(0, len(scores)-1)):
		if scores[i] > scores[i+1]:
			rewards[i] = max(rewards[i], rewards[i+1]+1)
	return sum(rewards)
