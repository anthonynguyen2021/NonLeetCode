def indexEqualsValue(array):
	# Time = O(log n)
	# Space = O(1)
	index = -1
	left = 0
	right = len(array) - 1
	while left <= right:
		mid = (left + right) // 2
		if array[mid] == mid:
			index = mid
			right = mid-1
		elif array[mid] > mid:
			right = mid - 1
		else:
			left = mid + 1
	return index 
