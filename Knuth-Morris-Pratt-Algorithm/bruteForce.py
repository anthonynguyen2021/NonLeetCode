# Time = O(mn) | Space = O(1)
def knuthMorrisPrattAlgorithm(string, substring):
    for i in range(len(string)):
		if substringMatch(string, substring, i):
			return True
	return False

def substringMatch(string, substring, i):
	if len(string) - i < len(substring):
		return False
	left, right = i, 0
	while right < len(substring) and string[left] == substring[right]:
		left += 1
		right += 1
	if right == len(substring):
		return True
	else:
		return False
