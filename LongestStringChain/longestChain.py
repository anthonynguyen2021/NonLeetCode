# Time = O(nlogn + nm^2) | Space = O(mn)
def longestStringChain(strings):
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
			if stringChains[smallerString]['maxChain']+1 > stringChains[string]['maxChain']:
				stringChains[string]['maxChain'] = stringChains[smallerString]['maxChain']+1
				stringChains[string]['next'] = smallerString

def buildLongestStringChain(strings, stringChains):
	# Find largest Chain size
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
