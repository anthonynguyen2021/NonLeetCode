

# Time = O(n) where n = len(array)
# Space = O(1)

# Idea of solution: Use the two pointer approach to sort largest element to the right. Set left = 0, right = len(array) - 1. This is just the first pass. The second pass will sort
# the remaining elements order[0], order[1] using the two pointer approach. 
def threeNumberSort(array, order):
	moveLargest(array, order)
	twoNumberSort(array, order)
	return array


def twoNumberSort(array, order):

	left = 0
	right = len(array) - 1

	while left <= right and array[right] == order[2]:
		right -= 1

	while True:

		while left <= right and (array[left] == order[0]):
			left +=1

		while left <= right and (array[right] == order[1]):
			right -=1

		if left > right:
			break

		array[left], array[right] = array[right], array[left]


def moveLargest(array, order):

	left = 0
	right = len(array) - 1

	while True:

		while left <= right and array[right] == order[2]:
			right -= 1

		while left <= right and array[left] != order[2]:
			left += 1

		if left > right:
			break

		array[left], array[right] = array[right], array[left]
