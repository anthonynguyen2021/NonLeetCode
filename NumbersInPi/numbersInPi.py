# Time = O() | Space = O()
def numbersInPi(pi, numbers):
    setNumbers = {number for number in numbers}
	cache = {}
	minSpace = getMinSpace(pi, setNumbers, cache, 0)
	return -1 if minSpace == float('inf') else minSpace

def getMinSpace(pi, setNumbers, cache, idx):
	if idx == len(pi):
		return -1
	elif idx in cache:
		return cache[idx]
	else:
		minSpace = float('inf')
		for i in range(idx, len(pi)):
			substring = pi[idx: i+1]
			if substring in setNumbers:
				minSubstring = getMinSpace(pi, setNumbers, cache, i+1)
				minSpace = min(minSpace, minSubstring+1)
		cache[idx] = minSpace
		return cache[idx]
