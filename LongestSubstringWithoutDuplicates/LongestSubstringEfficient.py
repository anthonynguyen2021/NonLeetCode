

def longestSubstringWithoutDuplication(string):
	'''
	Time: O(N) where N = length of the string
	Space: O(min(A, N)) where A is the length of the # of distinct characters in string

	The logic can be derivted as follows:

	1. By induction, at index i, ask if you've seen character string[i] before index i. If not, do nothing.
	If so, move the startIdx to max(startIdx, seen[char] + 1) - this means either the seen[char]'s index is 
	to the right of startIdx or seen[char]'s index is at most startIdx. Note: startIdx is the start of the 
	substring you're considering. Next, we check the length of the current substring in question and update
	longest substring; we update the index of the last time we've seen chara, which is i;
	the order of these two don't matter

	2. Next, check if the length of the substring string[startIdx: i+1] is the largest you've seen. If so
	record it.

	3. Update seen[char]'s index to index i. This says that you've last seen char at index i. 
	'''
	startIdx = 0
	seen = dict()
	longest = [0, 1]

	for i, char in enumerate(string):

		if char in seen:
			startIdx = max(startIdx, seen[char] + 1)

		seen[char] = i

		if i - startIdx + 1 > longest[1] - longest[0]:
			longest = [startIdx, i + 1]

	return string[longest[0]:longest[1]]
