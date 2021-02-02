# Time = O(n)
# Space = O(min(A, n)) where A is the # of distinct characters in string. 

# Idea: Use two pointers as a moving window to track when we've first seen a duplicate (say char) with the right
# pointer. Then move the left pointer one index over the first instance you see char. Make sure to progress
# the right pointer. If you haven't seen a duplicate, add it to the set. Then move the right pointer.
# Now check if the length of the substring string[left:right] is the current largest or not. 
def longestSubstringWithoutDuplication(string):
    if not string:
		return ""
	left = right = 0
	longest = [0, 1]
	seen = set()
	while right < len(string):
		if string[right] in seen:
			while string[left] != string[right]:
				seen.remove(string[left])
				left += 1
			left += 1
		else:
			seen.add(string[right])
		right += 1
		if right - left > longest[1] - longest[0]:
			longest = [left, right]
	return string[longest[0]:longest[1]]
