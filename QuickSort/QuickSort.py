# Time = O(nlogn) where n = len(array)
# Space = O(logn) - recursive calls
def quickSort(array):
	recurseQS(array, 0, len(array) - 1)
	return array

def recurseQS(array, left, right):
	if left < right:
		mid = partition(array, left, right)
		recurseQS(array, left, mid - 1)
		recurseQS(array, mid + 1, right)


def partition(array, left, right):

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
