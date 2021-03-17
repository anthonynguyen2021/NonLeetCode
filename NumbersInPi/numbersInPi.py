# Explanation: The idea of the recursive function does the following: Looking at substring of pi from index i to the end, we compute the smallest partition size so each part
# is in numbers. Note that at index 0, you look at substring pi[0:0+1], pi[0:1+1], ...., pi[0:len(pi)]. At index 1, you look at pi[1:1+1], pi[1:2+1], ..., pi[1:len(pi)], and so on.
# For each index, we have n^2, (n-1)^2, ... , 1^2 such substrings of pi. This sums to O(n^3). Note that at index 0, you'll call the function once in the main function. At index 1,
# you'll call the function at most once; at index 2, at most 2 times; and so on. This implies that the function calls is at most O(n^2). But due to caching, it'll reduce unnecessary
# computation. Note the lm comes from the setNumbers set since each key on average is l length and we have m of them. The space comes from the cache and setNumbers. For the base case
# in the recursive call, we have -1 since at idx = len(pi)-1, we have a letter that may be in numbers. But we know this has solution 0, so minSpace should be 0. According to our
# formula for minSpace, setting the result to -1 solves this.


# Time = O(n^3 + lm) | Space = O(n+ lm) where n is the length of pi, m is the length of numbers and l is the expected value of the length of numbers.

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
