# Idea of solution: We square each element and sort in place with no additional storage.

# Time = O(nlog n)
# Space = O(1)
def sortedSquaredArray(array):
    array = [val ** 2 for val in array]
	array.sort()
	return array
