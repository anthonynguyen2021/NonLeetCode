# Time = O(2^(m+n))
# Space = O(m+n)
def interweavingStrings(one, two, three):
    if len(one) + len(two) != len(three):
		return False
	return recurrenceWeave(one, two, three, 0, 0)

def recurrenceWeave(one, two, three, i, j):
	if i+j == len(one) + len(two):
		return True
	
	if i < len(one) and one[i] == three[i+j]:
		if recurrenceWeave(one, two, three, i+1, j):
			return True
	
	if j < len(two) and two[j] == three[i+j]:
		if recurrenceWeave(one, two, three, i, j+1):
			return True
	
	return False
