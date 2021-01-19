# Time = O(n)
# Space = O(1)
def quickselect(array, k):
	left = 0
	right = len(array) - 1
	while True:
		idx = partition(array, left, right)
		if idx == k-1:
			return array[idx]
		elif idx > k-1:
			right = idx-1
		else:
			left = idx+1
	
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

# For the worst case, we can initially check if the list is sorted or not by a linear scan. 
