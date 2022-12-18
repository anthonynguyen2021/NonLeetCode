

def longestStringChain(strings):
	'''
	Idea of solution:

	If we can sort our array by size, this will make DP more obvious. Suppose for the sake of argument that
	we have strings of size 1, 2, 3, ... , n. Then at string of length i, we can remove index 0, 1, ..., i - 1 and see if the smaller
	string is in our hashtable (which we constring for each string in strings) which has the largest chain seen so far for the 
	smallest string and the next string it points to as part of the chain. By default, we set our max chain size to 1 and next points to
	"".

	Explanation of complexity:

	For space, stringChains is O(nm) where n is the length of strings and m is the largest length of the string
	in strings. Also, sortedString is O(nm). At the end, building our longest chain is O(n * m).

	Time: O(nlogn + nm^2)
	Space: O(mn)
	'''
	stringChains = {}
	
	for string in strings:
		stringChains[string] = {'next': "", 'maxChain': 1}
	
	sortedString = sorted(strings, key=len)

	for string in sortedString:
		buildStringDictionary(string, stringChains)

	return buildLongestStringChain(strings, stringChains)


def buildStringDictionary(string, stringChains):

	for currentIdx in range(len(string)):

		smallerString = string[:currentIdx] + string[currentIdx+1 :]

		if smallerString in stringChains:

			if stringChains[smallerString]['maxChain'] + 1 > stringChains[string]['maxChain']:
				stringChains[string]['maxChain'] = stringChains[smallerString]['maxChain'] + 1
				stringChains[string]['next'] = smallerString


def buildLongestStringChain(strings, stringChains):
	'''Find largest Chain size'''
	maxChainSize = 1
	currentString = ""

	for string in strings:

		if stringChains[string]['maxChain'] > maxChainSize:
			maxChainSize = stringChains[string]['maxChain']
			currentString = string

	ourLargestChain = []

	while currentString != "":

		ourLargestChain.append(currentString)
		currentString = stringChains[currentString]['next']

	return ourLargestChain
