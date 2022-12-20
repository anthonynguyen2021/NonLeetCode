

def quickselect(array, k):
	'''
	Time: O(n) where n = len(array)
	Space: O(1)
	'''
	left = 0
	right = len(array) - 1

	while True:

		idx = partition(array, left, right)

		if idx == k - 1:
			break
		elif idx > k - 1:
			right = idx - 1
		else:
			left = idx + 1

	return array[idx]

	
def partition(array, left, right):

	if left == right:
		return left

	pivotVal = array[left]
	first = left + 1
	last = right 

	while True:

		while first <= last and array[first] <= pivotVal:
			first += 1

		while first <= last and array[last] >= pivotVal:
			last -= 1

		if first > last:
			break

		array[first], array[last] = array[last], array[first]

	array[left], array[last] = array[last], array[left]

	return last 
