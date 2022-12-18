

def minRewards(scores):
	'''
	Time: O(n) where n = len(scores)
	Space: O(n)
	'''
	if len(scores) == 1:
		return 1
	elif len(scores) == 2:
		return 3

	rewards = [1 for _ in scores]
	localMinIdx = getLocalMinIdx(scores)

	for index in localMinIdx:
		addRewardsLocalMin(scores, rewards, index)

	return sum(rewards)


def addRewardsLocalMin(scores, rewards, index):

	left, right = index - 1, index + 1

	while left >= 0 and scores[left] > scores[left+1]:
		rewards[left] = max(rewards[left], rewards[left+1]+1)
		left -= 1

	while right < len(scores) and scores[right-1] < scores[right]:
		rewards[right] = rewards[right-1] + 1
		right += 1


def getLocalMinIdx(scores):
	'''handles the case when len(scores) == 1 in main function and length 2'''
	localMinIdx = []

	for i in range(len(scores)):

		if i == 0 and scores[i] < scores[i+1]:
			localMinIdx.append(i)
		elif 0 < i < len(scores) - 1 and scores[i-1] > scores[i] and scores[i] < scores[i+1]:
			localMinIdx.append(i)
		elif i == len(scores) - 1 and scores[i-1] > scores[i]:
			localMinIdx.append(i)

	return localMinIdx
