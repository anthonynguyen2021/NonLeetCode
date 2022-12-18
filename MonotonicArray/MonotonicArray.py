

def isMonotonic(array):
	'''
	Time: O(n) where n = len(array)
	Space: O(1)
	'''
	increase = True
	decrease = True

	for idx in range(len(array) - 1):

		if array[idx] > array[idx+1]:
			increase = False

		if array[idx] < array[idx+1]:
			decrease = False

	return increase or decrease
