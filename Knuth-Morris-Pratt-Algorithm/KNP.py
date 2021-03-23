# Time = O(n+m) time | O(m) space where n = len(string) and m = len(substring)
def knuthMorrisPrattAlgorithm(string, substring):
    	pattern = buildPattern(substring)
	return doesMatch(string, substring, pattern)

def buildPattern(substring):
	pattern = [-1 for char in substring]
	j, i = 0, 1
	while i < len(substring):
		if substring[i] == substring[j]:
			pattern[i] = j
			i += 1
			j += 1
		elif j > 0:
			j = pattern[j-1] + 1
		else:
			i += 1
	return pattern

def doesMatch(string, substring, pattern):
	i, j = 0, 0
	while len(substring) - j <= len(string) - i:
		if string[i] == substring[j]:
			if j == len(substring) - 1:
				return True
			i += 1
			j += 1
		elif j > 0:
			j = pattern[j-1] + 1
		else:
			i += 1
	return False
