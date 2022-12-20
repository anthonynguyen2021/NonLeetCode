# Explanation: Space is O(m) since we're building an array of patterns where the entries represent the last time we saw a pattern
#  - i.e. the prefix at substring at index pattern[j-1] equals substring at index j. The idea is intiailize pattern with -1's, so when we have to update j = pattern[j-1]+1, 
# we might want to start at the beginning so that pattern[j-1] = -1, so j = 0. Note the pattern at
# index 0 is always -1. When substring at index j and i equal (prefix and suffix), increment both i, j. Otherwise, when j > 0, the pattern failed for 
# substring at index j and i. So go back to index pattern[j-1] and the entry of substring at this index equals index i-1. But we move to index j = pattern[j-1]+1.
# This part of the algorithm says when we decrement j to pattern[j-1]+1, we don't have to go to the beginning of substring and start at some portion of substring 
# that has been matched already. Otherwise, j = 0 and we have no patterns. Increment i. This steps says we look for the substring in string[i+1:] since the previous indices
# of string for j in {0, ... , i} was not successfuly in locating parts of substring.

# Note: We start with j = 0, i = 1 in the buildPatterns and NOT at i = j = 0 since we're looking for patterns at distinct indices.


# Explanation - Space is O(m) to build patterns. For Time, to see why it's O(n+m), just think that we decrement j back the same number of times we move i forward and i moves forward only.
# The proof idea is that over the course of the algorithm, the number of decrements of j can't exceed the increments of j, which is about the same number of increment of i (or less).
# due to the case of j > 0. 
# Time = O(n + m) time | O(m) space where n = len(string) and m = len(substring)
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
		# Check the previous point where index pattern[j-1] equals index i and we continue to check the substring at index pattern[j - 1] + 1
		elif j > 0:
			j = pattern[j - 1] + 1
		else:
			i += 1

	return pattern


def doesMatch(string, substring, pattern):
	i, j = 0, 0

	# As long as the length of substring[j:] is less than length of string[i:], do this.
	while len(substring) - j <= len(string) - i:

		# At the point we have a pattern - prefix equals suffix, check if j is at the end.
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
