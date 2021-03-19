# Time = O(n^2) | Space = O(n^2) 
def palindromePartitioningMinCuts(string):
	palindrome = [[False for _ in string] for _ in string]
	for i in range(len(string)):
		palindrome[i][i] = True
	for length in range(2, len(string)+1):
		for startIdx in range(0, len(string) - (length - 1)):
			endIdx = startIdx + length - 1
			if length == 2:
				palindrome[startIdx][endIdx] = string[startIdx] == string[endIdx]
			else:
				if string[startIdx] == string[endIdx] and palindrome[startIdx+1][startIdx+(length-1)-1]:
					palindrome[startIdx][endIdx] = True
    cuts = [float('inf') for char in string]
	cuts[0] = 0
	for idx in range(1, len(string)):
		if palindrome[0][idx]:
			cuts[idx] = 0
		else:
			for i in range(1, idx+1):
				if palindrome[i][idx]:
					cuts[idx] = min(cuts[idx], 1 + cuts[i-1])
	return cuts[-1]

def isPalindrome(string, i, j):
	found = True
	left, right = i, j
	while left < right:
		if string[left] != string[right]:
			found = False
			break
		left += 1
		right -= 1
	return found
